import pytest
from evercraft.models.character import Character, Alignment

#### Feature: Create a Character
# > As a character I want to have a name so that I can be distinguished 
# from other characters - multiple characters
# - can get and set Name

def test_create_character_class():
    c = Character()
    assert isinstance(c, Character)

def test_create_character_with_name_setter():
    character_name = "Cletus"
    c = Character()
    c.name = character_name
    assert c.name == character_name

def test_create_character_with_default_name():
    character_name = "Cletus"
    c = Character({"_name": character_name})
    assert c.name == character_name

def test_create_multiple_characters_with_diff_names():
    c1 = Character({"_name": "Cletus"})
    c2 = Character()
    c2.name = "Fred"
    assert c1.name != c2.name

def test_create_character_with_default_alignment():
    c = Character()
    assert c.alignment == Alignment.NEUTRAL

def test_create_character_set_alignment():
    alignment = Alignment.EVIL
    c = Character()
    c.alignment = alignment
    assert c.alignment == alignment

def test_create_character_with_all_attributes():
    attr = {
        "_name": "Thanos",
        "_alignment": Alignment.EVIL
    }
    thanos = Character(attr)
    assert thanos.name == "Thanos" and thanos.alignment == Alignment.EVIL
    