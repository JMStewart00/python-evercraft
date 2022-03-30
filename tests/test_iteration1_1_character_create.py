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
    c = Character({"name": character_name})
    assert c.name == character_name

def test_create_multiple_characters_with_diff_names():
    c1 = Character({"name": "Cletus"})
    c2 = Character()
    c2.name = "Fred"
    assert c1.name != c2.name

    