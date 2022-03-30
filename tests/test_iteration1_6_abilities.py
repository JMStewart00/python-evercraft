import pytest
from evercraft.models.character import Character
from evercraft.models.ability import Ability, AbilityType

def test_character_has_abilities_list():
    c = Character()
    assert type(c.abilities) == list

def test_ability_score_has_correct_mod_score_for_15():
    ability_score = Ability(AbilityType(1))
    ability_score.update_attributes(15)
    assert ability_score.score == 15 and ability_score.mod == 2

def test_ability_score_has_correct_mod_score_for_2():
    ability_score = Ability(AbilityType(5))
    ability_score.update_attributes(2)
    assert ability_score.score == 2 and ability_score.mod == -4

def test_ability_score_has_correct_mod_score_for_10():
    ability_score = Ability(AbilityType(4))
    ability_score.update_attributes(10)
    assert ability_score.score == 10 and ability_score.mod == 0