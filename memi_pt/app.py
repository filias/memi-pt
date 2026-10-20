"""Memi Portugal - practise your memory of Portugal."""

from memi_engine import MemiConfig, create_app

# Import providers to register them
import memi_pt.providers  # noqa: F401

# The game in English, at /en/ (memi-engine's MemiConfig.languages): every
# field below that's in Portuguese, and what the menu calls each category.
# The cards' answers and tags are translated by each provider.
ENGLISH = {
    "subtitle": "practise your memory",
    "sponsor_text": "sponsor",
    "label_related_sites": "more memi games",
    "about_html": """
        <p>Memi Portugal is a memory game about Portugal. Districts,
        monuments, food, famous people &mdash; there's always something new
        to learn.</p>

        <h2>How to play</h2>
        <p>Pick a category, look at the picture and try to name it before
        revealing the answer. No accounts, no scores, no time limits.</p>
        <p>The bottom bar has a few helpers:</p>
        <ul>
            <li><strong>clues:</strong> turns on progressive letter clues
            &mdash; show the first letter, then the next, and so on. Handy
            when the name is on the tip of your tongue.</li>
            <li><strong>know more:</strong> appears on reveal and opens the
            item's Wikipedia article (or its source page), so you can read
            more.</li>
            <li><strong>report:</strong> flags a card whose picture doesn't
            match the answer (wrong image, broken thumbnail, etc.).</li>
        </ul>
        <p>You can play in two ways:</p>
        <ul>
            <li><strong>To learn:</strong> when you don't recognise
            something, reveal the answer and follow <em>know more</em> to
            read about it. Each exposure strengthens the link between the
            picture and the name.</li>
            <li><strong>To test yourself:</strong> once a category feels
            familiar, go through it and see how many you can name without
            revealing.</li>
        </ul>

        <h2>Why it works</h2>
        <p>It's a simple form of <em>active recall</em> &mdash; pulling
        information out of memory instead of re-reading it. The
        <em>testing effect</em>, well documented in cognitive psychology,
        shows that retrieval practice builds more durable memories than
        re-exposure alone.</p>
        <p>Because each prompt is a picture, the game also leans on the
        <em>picture superiority effect</em>: pictures are encoded more
        richly than words and are easier to recall later. Naming the item
        is a form of <em>cued recall</em>, between simple recognition
        (&ldquo;have I seen this before?&rdquo;) and unaided <em>free
        recall</em>.</p>
        <p>Short, frequent sessions work better than long ones &mdash; the
        <em>spacing effect</em>. A few minutes a day is enough.</p>

        <h2>Credits</h2>
        <p>Images and descriptions from Wikipedia and Wikimedia Commons, under
        their Creative Commons licences. The language recordings are by
        native speakers of European Portuguese for
        <a href="https://lingualibre.org">Lingua Libre</a> (CC BY-SA 4.0; see
        <a href="https://github.com/filias/memi-pt/blob/main/static/audio/CREDITS.md">CREDITS.md</a>).
        Maps &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>
        contributors.</p>
    """,
    "label_theme": "theme",
    "label_about": "about",
    "label_report": "report",
    "label_reported": "reported",
    "label_clues_on": "clues: on",
    "label_clues_off": "clues: off",
    "label_show_letter": "show letter",
    "label_pick_category": "pick a category",
    "label_loading": "loading...",
    "label_all_done": "all done! click to start over",
    "label_click_to_reveal": "click the image to reveal the answer",
    "label_click_for_new": "click again for a new one",
    "label_back": "back to playing",
    "label_more": "know more",
    "label_open_map": "open map",
    "label_listen": "listen",
    "label_all": "all",
    "label_contents": "what's in this category",
    "category_labels": {
        "cultura": "culture",
        "geografia": "geography",
        "língua": "language",
        "natureza": "nature",
        "pessoas": "people",
        "monumentos": "monuments",
        "comida": "food",
        "clubes": "clubs",
        "pinturas": "paintings",
        "distritos": "districts",
        "cidades": "cities",
        "rios": "rivers",
        "animais": "animals",
        "plantas": "plants",
        "antes de 1143": "before 1143",
        "monarquia 1143-1910": "monarchy 1143-1910",
        "república 1910-presente": "republic 1910-present",
        "português → inglês": "portuguese → english",
        "inglês → português": "english → portuguese",
    },
}

# The home page opens on the menu, and its empty card shows Portugal's outline
# in its flag above "escolhe uma categoria" ("pick a category" at /en/). The
# engine has no setting for
# that, so this rides on analytics_html (raw HTML at the bottom of every page,
# after app.js); loading a category replaces the card's text, so the map goes
# with it. static/flag-map-portugal.svg: Wikimedia Commons, "Flag map of
# Portugal.svg", public domain.
HOME_CARD_HTML = """
<style>
    #status.home { width: 100%; text-align: center; }
    #status .home-map { display: block; max-width: 80%; max-height: calc(min(500px, 90vw) * 0.6); margin: 0 auto 1.5rem; }
</style>
<script>
(function () {
    var status = document.getElementById('status');
    var label = status && status.textContent.trim();
    if (label === 'escolhe uma categoria' || label === 'pick a category') {
        status.classList.add('home');
        status.insertAdjacentHTML('afterbegin', '<img class="home-map" src="/static/flag-map-portugal.svg" alt="Portugal">');
    }
})();
</script>
"""

config = MemiConfig(
    analytics_html=(
        '<script data-goatcounter="https://memi-pt.goatcounter.com/count"'
        ' async src="//gc.zgo.at/count.js"></script>'
    ) + HOME_CARD_HTML,
    # What the page tells Google and screen readers it is: this game
    # is Portuguese, not the engine's default English.
    html_lang="pt",
    # Details panel beside the card on reveal: the Wikipedia intro (in
    # Portuguese where it exists) and, for places, a map.
    layout="enriched",
    title="memi portugal",
    subtitle="pratica a tua memória",
    favicon_color="#006600",
    sponsor_url="https://github.com/sponsors/filias",
    sponsor_text="apoiar",
    related_sites=[
        {"name": "memi", "url": "https://world.memi.games"},
        {"name": "memi lisboa", "url": "https://lx.memi.games"},
        {"name": "memi slovensko", "url": "https://sk.memi.games"},
        {"name": "memi united states", "url": "https://us.memi.games"},
    ],
    label_related_sites="outros jogos memi",
    about_html="""
        <p>Memi Portugal é um jogo de memória sobre Portugal. Distritos,
        monumentos, comida, pessoas famosas &mdash; há sempre algo novo
        para aprender.</p>

        <h2>Como jogar</h2>
        <p>Escolhe uma categoria, olha para a imagem e tenta adivinhar
        o que é antes de revelar a resposta. Sem contas, sem pontuação,
        sem limite de tempo.</p>
        <p>Na barra inferior tens alguns auxiliares:</p>
        <ul>
            <li><strong>pistas:</strong> ativa pistas progressivas de
            letras &mdash; revela a primeira letra, depois a seguinte, e
            assim por diante. Útil quando o nome está na ponta da
            língua.</li>
            <li><strong>saber mais:</strong> aparece ao revelar e abre o
            artigo da Wikipédia (ou a página da fonte) do item, para que
            possas ler mais.</li>
            <li><strong>reportar:</strong> marca uma carta se a imagem não
            corresponder à resposta (imagem errada, miniatura partida,
            etc.).</li>
        </ul>
        <p>Podes jogar de duas formas:</p>
        <ul>
            <li><strong>Para aprender:</strong> quando não reconheces um
            item, revela a resposta e segue o link <em>saber mais</em>
            para ler sobre ele. Cada exposição reforça a associação entre
            a imagem e o nome.</li>
            <li><strong>Para te testares:</strong> quando uma categoria já
            te é familiar, percorre-a e vê quantas consegues nomear sem
            revelar.</li>
        </ul>

        <h2>Porque funciona</h2>
        <p>Esta é uma forma simples de <em>recordação ativa</em> &mdash;
        recuperar informação da memória em vez de a reler. O <em>efeito
        de teste</em>, bem documentado em psicologia cognitiva, mostra
        que a prática de recuperação cria memórias mais duradouras do que
        a simples re-exposição.</p>
        <p>Como cada estímulo é uma imagem, o jogo aproveita também o
        <em>efeito de superioridade da imagem</em>: as imagens são
        codificadas de forma mais rica do que as palavras e mais fáceis
        de recuperar depois. Nomear o item é uma forma de
        <em>recordação com pista</em>, situada entre o reconhecimento
        simples (&ldquo;já vi isto antes?&rdquo;) e a
        <em>recordação livre</em> sem ajuda.</p>
        <p>Sessões curtas e frequentes funcionam melhor do que sessões
        longas &mdash; o <em>efeito de espaçamento</em>. Alguns minutos
        por dia chegam.</p>

        <h2>Créditos</h2>
        <p>Imagens e descrições da Wikipédia e da Wikimedia Commons, com as
        suas licenças Creative Commons. As gravações da categoria língua são de
        falantes nativos de português europeu para o
        <a href="https://lingualibre.org">Lingua Libre</a> (CC BY-SA 4.0; ver
        <a href="https://github.com/filias/memi-pt/blob/main/static/audio/CREDITS.md">CREDITS.md</a>).
        Mapas &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>.</p>
    """,
    # Portuguese labels
    label_theme="tema",
    label_about="sobre",
    label_report="reportar",
    label_reported="reportado",
    label_clues_on="pistas: sim",
    label_clues_off="pistas: não",
    label_show_letter="mostrar letra",
    label_pick_category="escolhe uma categoria",
    label_loading="a carregar...",
    label_all_done="tudo feito! clica para recomeçar",
    label_click_to_reveal="clica na imagem para revelar a resposta",
    label_click_for_new="clica novamente para outra",
    label_back="voltar a jogar",
    label_more="saber mais",
    label_open_map="abrir mapa",
    label_listen="ouvir",
    label_all="todos",
    label_contents="o que há nesta categoria",
    languages={"en": ENGLISH},
    done_html="""
        <svg width="200" height="180" viewBox="0 0 80 72" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <clipPath id="heart-clip">
                    <path d="M40 68 C40 68 4 44 4 22 C4 10 14 2 24 2 C30 2 36 6 40 12 C44 6 50 2 56 2 C66 2 76 10 76 22 C76 44 40 68 40 68Z"/>
                </clipPath>
            </defs>
            <g clip-path="url(#heart-clip)">
                <rect x="0" y="0" width="32" height="72" fill="#006600"/>
                <rect x="32" y="0" width="48" height="72" fill="#FF0000"/>
            </g>
            <path d="M40 68 C40 68 4 44 4 22 C4 10 14 2 24 2 C30 2 36 6 40 12 C44 6 50 2 56 2 C66 2 76 10 76 22 C76 44 40 68 40 68Z"
                  fill="none" stroke="var(--subtle, #888)" stroke-width="1.5"/>
        </svg>
    """,
)

import os
from flask import redirect

instance_static = os.path.join(os.path.dirname(__file__), "..", "static")
app = create_app(config, instance_static=instance_static)

# The people eras were renamed so the menu (sorted A-Z) reads in date order;
# their old addresses were already out there, so they still lead to them.
_OLD_SLUGS = {
    "1143-1910": "monarquia-1143-1910",
    "1910-presente": "republica-1910-presente",
}
for _old, _new in _OLD_SLUGS.items():
    for _prefix in ("", "/en"):
        app.add_url_rule(
            f"{_prefix}/{_old}",
            f"old_slug{_prefix.replace('/', '_')}_{_old}",
            lambda to=f"{_prefix}/{_new}": redirect(to, code=301),
        )

if __name__ == "__main__":
    app.run(debug=True, port=8090)
