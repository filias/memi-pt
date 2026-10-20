"""Everyday European Portuguese for visitors: about 25 useful words and phrases."""

import re
import unicodedata

PHRASES = {
    "hello": "olá",
    "good morning": "bom dia",
    "good afternoon": "boa tarde",
    "good evening / good night": "boa noite",
    "goodbye": "adeus",
    "see you later": "até logo",
    "thank you (said by a man)": "obrigado",
    "thank you (said by a woman)": "obrigada",
    "please": "por favor",
    "you're welcome": "de nada",
    "yes": "sim",
    "no": "não",
    "sorry / excuse me": "desculpe",
    "how are you?": "como está?",
    "cheers!": "saúde!",
    "enjoy your meal!": "bom apetite!",
    "I don't understand": "não percebo",
    "how much is it?": "quanto custa?",
    "the bill, please": "a conta, por favor",
    "help!": "socorro!",
    "water": "água",
    "beer": "cerveja",
    "wine": "vinho",
    "coffee": "café",
    "friend": "amigo",
    "love": "amor",
    "congratulations!": "parabéns!",
    "welcome": "bem-vindo",
}

# For the details panel: how to say it (stress in capitals) and when to use it.
# European Portuguese swallows unstressed vowels, so many words sound shorter
# than they look.
PHRASE_NOTES = {
    "olá": ("oh-LAH", "Hello, at any time of day."),
    "bom dia": ("bong DEE-uh", "Good morning, until lunch. The \"om\" is nasal."),
    "boa tarde": ("BOH-uh TARD", "Good afternoon, from lunch until it gets dark."),
    "boa noite": ("BOH-uh NOYT", "Good evening and good night — both hello and goodbye after dark."),
    "adeus": ("uh-DEH-oosh", "Goodbye. Final-sounding; for every day, até logo is more usual."),
    "até logo": ("uh-TEH LOH-goo", "See you later — the everyday goodbye."),
    "obrigado": ("oh-bree-GAH-doo", "Thank you, if you're a man: it agrees with the speaker, not the listener."),
    "obrigada": ("oh-bree-GAH-duh", "Thank you, if you're a woman."),
    "por favor": ("poor fuh-VOR", "Please. In a café you'll also hear se faz favor."),
    "de nada": ("deh NAH-duh", "You're welcome; literally \"of nothing\"."),
    "sim": ("seeng", "Yes. The m is barely there: a nasal \"ee\"."),
    "não": ("nowng", "No — a nasal \"ow\". Also \"not\": não sei, \"I don't know\"."),
    "desculpe": ("dish-KOOLP", "Sorry, or excuse me to get someone's attention. To a friend: desculpa."),
    "como está?": ("KOH-moo ish-TAH", "How are you? — polite. To a friend: como estás? or tudo bem?"),
    "saúde!": ("suh-OOD", "Cheers! Literally \"health\" — also said when someone sneezes."),
    "bom apetite!": ("bong uh-peh-TEET", "Enjoy your meal — said as the food arrives."),
    "não percebo": ("nowng per-SEH-boo", "I don't understand. Add mais devagar, por favor — \"slower, please\"."),
    "quanto custa?": ("KWAN-too KOOSH-tuh", "How much is it?"),
    "a conta, por favor": ("uh KON-tuh poor fuh-VOR", "The bill, please."),
    "socorro!": ("soo-KOH-roo", "Help! Emergency number in Portugal: 112."),
    "água": ("AH-gwuh", "Water. Sem gás is still, com gás is sparkling."),
    "cerveja": ("ser-VAY-zhuh", "Beer. A small draught is uma imperial in Lisbon, um fino in Porto."),
    "vinho": ("VEE-nyoo", "Wine: tinto (red), branco (white), verde (young, from the Minho)."),
    "café": ("kuh-FEH", "Coffee — an espresso. In Lisbon also uma bica."),
    "amigo": ("uh-MEE-goo", "Friend; a woman friend is amiga."),
    "amor": ("uh-MOR", "Love — and what couples call each other."),
    "parabéns!": ("puh-ruh-BAYNGSH", "Congratulations! — and happy birthday."),
    "bem-vindo": ("bayng-VEEN-doo", "Welcome; to a woman, bem-vinda."),
}

# Native recordings on Wikimedia Commons, from Lingua Libre (European
# Portuguese). Speakers and licences are in static/audio/CREDITS.md; phrases
# missing here use the browser's voice.
RECORDINGS = {
    "olá": "LL-Q5146 (por)-Santamarcanda-olá.wav",
    "adeus": "LL-Q5146 (por)-Santamarcanda-adeus.wav",
    "obrigado": "LL-Q5146 (por)-Santamarcanda-obrigado.wav",
    "obrigada": "LL-Q5146 (por)-Santamarcanda-obrigada.wav",
    "sim": "LL-Q5146 (por)-Santamarcanda-sim.wav",
    "não": "LL-Q5146 (por)-Santamarcanda-não.wav",
    "desculpe": "LL-Q5146 (por)-Santamarcanda-desculpe.wav",
    "saúde!": "LL-Q5146 (por)-Santamarcanda-saúde.wav",
    "socorro!": "LL-Q5146 (por)-Santamarcanda-socorro.wav",
    "água": "LL-Q5146 (por)-Santamarcanda-água.wav",
    "cerveja": "LL-Q5146 (por)-Santamarcanda-cerveja.wav",
    "vinho": "LL-Q5146 (por)-Santamarcanda-vinho.wav",
    "café": "LL-Q5146 (por)-Santamarcanda-café.wav",
    "amigo": "LL-Q5146 (por)-Santamarcanda-amigo.wav",
    "amor": "LL-Q5146 (por)-Santamarcanda-amor.wav",
    "parabéns!": "LL-Q5146 (por)-Santamarcanda-parabéns.wav",
    "bem-vindo": "LL-Q5146 (por)-Santamarcanda-bem-vindo.wav",
}

# The same phrases keyed by their Portuguese, for the Portuguese → English direction.
ENGLISH = {portuguese: english for english, portuguese in PHRASES.items()}


def phrase_slug(portuguese):
    """``"como está?"`` -> ``"como-esta"`` (recording filename)."""
    folded = unicodedata.normalize("NFKD", portuguese)
    ascii_text = folded.encode("ascii", "ignore").decode().lower()
    return "-".join(re.findall(r"[a-z0-9]+", ascii_text))
