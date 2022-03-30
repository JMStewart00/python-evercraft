import pytest
from evercraft.models.character import Character, Alignment

def test_create_character_with_all_attributes():
    attr = {
        "alignment": Alignment.EVIL,
        "armor_class": 20,
        "hit_points": 50,
        "name": "Thanos",
    }
    thanos = Character(attr)
    assert (
        thanos.name == "Thanos" and
        thanos.alignment == Alignment.EVIL and
        thanos.armor_class == 20 and
        thanos.hit_points == 50
    )
