"""Portuguese category providers."""

import base64
from pathlib import Path
from urllib.parse import quote

from memi_engine import CategoryProvider, ScientificNameProvider, register
from memi_engine import images

from memi_pt.categories.cities import CITIES, WIKIPEDIA as CITY_WIKI, REGIONS as CITY_REGIONS
from memi_pt.categories.clubs import (
    CLUBS,
    LOGOS as CLUB_LOGOS,
    TAGS as CLUB_TAGS,
    WIKIPEDIA as CLUB_WIKI,
)
from memi_pt.categories.paintings import PAINTINGS, COMMONS_FILES as PAINTING_FILES, TAGS as PAINTING_TAGS
from memi_pt.categories.rivers import RIVERS, WIKIPEDIA as RIVER_WIKI, TAGS as RIVER_TAGS
from memi_pt.categories.districts import (
    DISTRICTS,
    MAP_FILES as DISTRICT_MAPS,
    WIKIPEDIA as DISTRICT_WIKI,
)
from memi_pt.categories.monuments import (
    MONUMENTS,
    LOCATIONS,
    WIKIPEDIA as MONUMENT_WIKI,
)
from memi_pt.categories.food import FOOD
from memi_pt.categories.language import ENGLISH, PHRASE_NOTES, PHRASES, phrase_slug
from memi_pt.categories.monarchy import (
    ALL as MONARCHY_ALL,
    WIKIPEDIA as MONARCHY_WIKI,
    TAGS as MONARCHY_TAGS,
)
from memi_pt.categories.pre_kingdom import (
    FIGURES as PRE_KINGDOM_ALL,
    WIKIPEDIA as PRE_KINGDOM_WIKI,
    TAGS as PRE_KINGDOM_TAGS,
)
from memi_pt.categories.republic import (
    ALL as REPUBLIC_ALL,
    WIKIPEDIA as REPUBLIC_WIKI,
    TAGS as REPUBLIC_TAGS,
)
from memi_pt.categories.nature import (
    ALL_ANIMALS,
    ALL_PLANTS,
    ANIMAL_WIKIPEDIA,
    PLANT_WIKIPEDIA,
    SCIENTIFIC_NAMES,
)

# Mainland Portugal, the Azores and Madeira. Wikidata coordinates outside it
# belong to something other than the place on the card, so they get no map.
PORTUGAL_BOUNDS = ((32.0, 42.2), (-31.6, -6.1))


class DistrictsProvider(CategoryProvider):
    key = "geografia:distritos"
    items = DISTRICTS
    override_name = True
    map_zoom = 8
    map_bounds = PORTUGAL_BOUNDS

    def get_image(self, item):
        map_file = DISTRICT_MAPS.get(item)
        if map_file:
            result = images.get_wikipedia_file_image(map_file)
            if result:
                return result
        return images.get_wikipedia_image(item)

    def get_wikipedia_title(self, item):
        # The card is a map file with no article link of its own.
        return ("en", DISTRICT_WIKI.get(item, item))


class MonumentsProvider(CategoryProvider):
    key = "cultura:monumentos"
    items = MONUMENTS
    override_name = True
    map_zoom = 16
    map_bounds = PORTUGAL_BOUNDS

    def get_image(self, item):
        wiki = MONUMENT_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return LOCATIONS.get(item)


class FoodProvider(CategoryProvider):
    key = "cultura:comida"
    items = FOOD

    def get_image(self, item):
        result = images.get_wikipedia_image(item)
        if not result or not result.get("image"):
            result = images.get_wikipedia_image(item + " (food)")
        return result


class MonarchyProvider(CategoryProvider):
    key = "pessoas:1143-1910"
    items = MONARCHY_ALL
    override_name = True

    def get_image(self, item):
        wiki = MONARCHY_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return MONARCHY_TAGS.get(item)


class RepublicProvider(CategoryProvider):
    key = "pessoas:1910-presente"
    items = REPUBLIC_ALL
    override_name = True

    def get_image(self, item):
        wiki = REPUBLIC_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return REPUBLIC_TAGS.get(item)


class AnimalsProvider(ScientificNameProvider):
    key = "natureza:animais"
    items = ALL_ANIMALS
    override_name = True
    scientific_names = SCIENTIFIC_NAMES

    def get_image(self, item):
        wiki = ANIMAL_WIKIPEDIA.get(item, item)
        return images.get_wikipedia_image(wiki)


class PlantsProvider(ScientificNameProvider):
    key = "natureza:plantas"
    items = ALL_PLANTS
    override_name = True
    scientific_names = SCIENTIFIC_NAMES

    def get_image(self, item):
        wiki = PLANT_WIKIPEDIA.get(item, item)
        return images.get_wikipedia_image(wiki)


class CitiesProvider(CategoryProvider):
    key = "geografia:cidades"
    items = CITIES
    override_name = True
    map_zoom = 12
    map_bounds = PORTUGAL_BOUNDS

    def get_image(self, item):
        wiki = CITY_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return CITY_REGIONS.get(item)


class PreKingdomProvider(CategoryProvider):
    key = "pessoas:antes de 1143"
    items = PRE_KINGDOM_ALL
    override_name = True

    def get_image(self, item):
        wiki = PRE_KINGDOM_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return PRE_KINGDOM_TAGS.get(item)


class RiversProvider(CategoryProvider):
    key = "geografia:rios"
    items = RIVERS
    override_name = True

    def get_image(self, item):
        wiki = RIVER_WIKI.get(item, item)
        result = images.get_river_map(wiki)
        if not result or not result.get("image"):
            result = images.get_wikipedia_image(wiki)
        return result

    def get_tag(self, item):
        return RIVER_TAGS.get(item)

    def get_wikipedia_title(self, item):
        # The card is often a river map with no article link. No map in the
        # panel: a river's Wikidata point is a single spot on it (its mouth).
        return ("en", RIVER_WIKI.get(item, item))


class ClubsProvider(CategoryProvider):
    key = "cultura:clubes"
    items = CLUBS
    override_name = True
    light_bg = True

    def get_image(self, item):
        logo = CLUB_LOGOS.get(item)
        if logo:
            return {"name": item, "image": logo}
        return images.get_wikipedia_image(item)

    def get_tag(self, item):
        return CLUB_TAGS.get(item)

    def get_wikipedia_title(self, item):
        # The card is a local logo with no article link.
        return ("en", CLUB_WIKI.get(item, item))


class PaintingsProvider(CategoryProvider):
    key = "cultura:pinturas"
    items = PAINTINGS
    override_name = True

    def get_image(self, item):
        filename = PAINTING_FILES.get(item)
        if filename:
            return images.get_commons_file_image(filename)
        return None

    def get_tag(self, item):
        return PAINTING_TAGS.get(item)



AUDIO_DIR = Path(__file__).resolve().parent.parent.parent / "static" / "audio"


def _text_card(text):
    """Render a short phrase as an SVG data-URI to use as the card image."""
    size = min(60, max(28, 780 // max(len(text), 1)))
    safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="420" '
        'viewBox="0 0 640 420">'
        '<rect width="640" height="420" fill="#f7f5f0"/>'
        f'<text x="320" y="140" text-anchor="middle" dominant-baseline="middle" '
        f"font-family=\"Georgia, 'Times New Roman', serif\" font-size=\"{size}\" "
        f'fill="#223344">{safe}</text>'
        "</svg>"
    )
    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return "data:image/svg+xml;base64," + b64


class EnglishToPortuguese(CategoryProvider):
    """For visitors: read the English, say the Portuguese."""

    key = "língua:inglês → português"
    light_bg = True
    items = list(PHRASES)

    def portuguese(self, item):
        return PHRASES[item]

    def get_image(self, item):
        portuguese = self.portuguese(item)
        return {
            "name": portuguese,
            "image": _text_card(item),
            "url": f"https://en.wiktionary.org/wiki/{quote(portuguese)}",
        }

    def get_details(self, item):
        say, note = PHRASE_NOTES[self.portuguese(item)]
        return {"text": f"Say: {say}\n\n{note}"}

    def get_audio(self, item):
        """The Portuguese, spoken: a native speaker's recording from
        static/audio/<slug>.mp3 when there is one, else the browser's voice."""
        portuguese = self.portuguese(item)
        audio = {"text": portuguese, "lang": "pt-PT"}
        recording = AUDIO_DIR / f"{phrase_slug(portuguese)}.mp3"
        if recording.exists():
            audio["src"] = f"/static/audio/{recording.name}"
        return audio


class PortugueseToEnglish(EnglishToPortuguese):
    """The other way round: read the Portuguese, name the English."""

    key = "língua:português → inglês"
    items = list(ENGLISH)
    submenu_default = True

    def portuguese(self, item):
        return item

    def get_image(self, item):
        return {**super().get_image(item), "name": ENGLISH[item]}

    def get_audio(self, item):
        # Hearing the Portuguese is part of the question here: listen, then answer.
        return {**super().get_audio(item), "before_reveal": True}


register(PreKingdomProvider())
register(DistrictsProvider())
register(CitiesProvider())
register(RiversProvider())
register(MonumentsProvider())
register(FoodProvider())
register(ClubsProvider())
register(PaintingsProvider())
register(MonarchyProvider())
register(RepublicProvider())
register(AnimalsProvider())
register(PlantsProvider())
register(PortugueseToEnglish())
register(EnglishToPortuguese())
