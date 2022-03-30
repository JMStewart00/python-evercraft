import pytest
from evercraft.models.character import Character, Alignment

def test_create_character_default_armor_class():
    defVal = 10
    c = Character()
    assert c.armor_class == defVal

def test_create_character_change_armor_class():
    defVal = 10
    c = Character({ "armor_class": 50 })
    assert c.armor_class != defVal

def test_create_character_default_hit_points():
    defVal = 5
    c = Character()
    assert c.hit_points == defVal

def test_create_character_change_hit_points():
    defVal = 5
    c = Character({ "hit_points": 20 })
    assert c.hit_points != defVal