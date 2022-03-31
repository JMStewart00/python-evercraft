import pytest
from random import randint

from evercraft.models.character import Character
from evercraft.models.ability import Ability, AbilityType

def test_character_has_abilities_list():
    c = Character()
    assert type(c.abilities) == list

def test_ability_score_has_correct_mod_score_for_15():
    ability_score = Ability(AbilityType(1))
    ability_score.adjust_score_and_mod(15)
    assert ability_score.score == 15 and ability_score.mod == 2

def test_ability_score_has_correct_mod_score_for_2():
    ability_score = Ability(AbilityType(5))
    ability_score.adjust_score_and_mod(2)
    assert ability_score.score == 2 and ability_score.mod == -4

def test_ability_score_has_correct_mod_score_for_10():
    ability_score = Ability(AbilityType(4))
    ability_score.adjust_score_and_mod(10)
    assert ability_score.score == 10 and ability_score.mod == 0

def test_character_can_update_strength():
    c = Character()
    
    a = AbilityType.STRENGTH.value
    score = randint(1, 20)

    c.update_ability(a, score)

    ability = c.find_ability(a)
    assert ability.score == score and ability.mod == Ability.SCORE_MODS.get(score)

def test_character_can_update_dexterity():
    c = Character()
    
    a = AbilityType.DEXTERITY.value
    score = randint(1, 20)

    c.update_ability(a, score)

    ability = c.find_ability(a)
    assert ability.score == score and ability.mod == Ability.SCORE_MODS.get(score)

def test_character_can_update_all_abilities():
    c = Character()
    for i in AbilityType:
        a = AbilityType(i)
        score = randint(1, 20)

        ability_index = a.value
        c.update_ability(ability_index, score)
        ability = c.find_ability(ability_index)

    assert ability.score == score and ability.mod == Ability.SCORE_MODS.get(score)

def test_character_can_set_strength_at_creation():
    score = 19
    c = Character(STRENGTH=score)

    a = AbilityType.STRENGTH.value
    c_ability = c.find_ability(a)
    assert c_ability.score == score and c_ability.mod == Ability.SCORE_MODS.get(score)

def test_character_doesnt_allow_values_outside_1_and_20():
    with pytest.raises(ValueError):
        c = Character(STRENGTH=-1, DEXTERITY=20, WISDOM=25)