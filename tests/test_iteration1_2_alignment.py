import pytest
from evercraft.models.character import Character, Alignment

# Feature: Alignment
# As a character I want to have an alignment so that I have something to guide my actions

# can get and set alignment
# alignments are Good, Evil, and Neutral

def test_create_character_with_default_alignment():
    c = Character()
    assert c.alignment == Alignment.NEUTRAL

def test_create_character_set_alignment():
    alignment = Alignment.EVIL
    c = Character()
    c.alignment = alignment
    assert c.alignment == alignment
