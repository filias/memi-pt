#!/usr/bin/env bash
# Run on the existing memi.click server (Caddy + uv + memi user already set up).
# Usage: WEBHOOK_SECRET=xxxx bash setup.sh
#
# Safe to run against the already-deployed pt.memi.click: it pulls if the repo
# is already cloned, and does not clobber a running game service on another port.
set -euo pipefail

: "${WEBHOOK_SECRET:?Set WEBHOOK_SECRET (the GitHub webhook secret) before running}"

REPO=https://github.com/filias/memi-pt.git
APP_DIR=/opt/memi-pt

# Clone or update (memi user already exists from the main memi setup)
if [ -d "$APP_DIR/.git" ]; then
    sudo -u memi git -C "$APP_DIR" pull
else
    git clone "$REPO" "$APP_DIR"
    chown -R memi:memi "$APP_DIR"
fi

cd "$APP_DIR"
sudo -u memi uv sync

# App service — only install if there isn't one already (don't disturb a running
# instance that may be bound to a different port).
if [ ! -f /etc/systemd/system/memi-pt.service ]; then
    cp deploy/memi-pt.service /etc/systemd/system/memi-pt.service
    systemctl enable memi-pt
fi

# Webhook service + secret
echo "WEBHOOK_SECRET=${WEBHOOK_SECRET}" > /etc/memi-pt-webhook.env
chmod 600 /etc/memi-pt-webhook.env
cp deploy/memi-pt-webhook.service /etc/systemd/system/memi-pt-webhook.service

systemctl daemon-reload
systemctl enable --now memi-pt-webhook
systemctl restart memi-pt   # pick up the code just pulled

# Add the pt.memi.click block to Caddy if missing. If pt.memi.click is already
# in the Caddyfile (it is, since the site already serves), add the /deploy
# handler to its existing block by hand instead — see the note printed below.
if ! grep -q "pt.memi.click" /etc/caddy/Caddyfile; then
cat >> /etc/caddy/Caddyfile <<'EOF'

pt.memi.click {
    handle /deploy {
        reverse_proxy localhost:9014
    }
    handle {
        reverse_proxy localhost:8092
    }
}
EOF
    systemctl reload caddy
else
    echo ""
    echo ">> pt.memi.click already in /etc/caddy/Caddyfile."
    echo ">> Add this INSIDE its block (before the catch-all reverse_proxy), then"
    echo ">> 'systemctl reload caddy':"
    echo ""
    echo "       handle /deploy {"
    echo "           reverse_proxy localhost:9014"
    echo "       }"
fi

echo ""
echo "Done."
echo "GitHub webhook: https://pt.memi.click/deploy  (content-type json, event push,"
echo "                secret = \$WEBHOOK_SECRET)"
