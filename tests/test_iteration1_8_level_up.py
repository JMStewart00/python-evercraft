import pytest
from random import randint

from evercraft.models.character import Character
from evercraft.models.ability import Ability, AbilityType
from evercraft.models.combat import Combat

def test_character_has_a_level():
    c = Character()
    assert hasattr(c, 'level')

def test_character_has_level_5_with_5125():
    c = Character({ "xp": 5125 })
    c.level_up()
    assert c.level == 5

def test_character_levels_up_to_3_after_2():
    c = Character({ "xp": 1995 })
    c.level_up()

    roll = 19
    defn = Character({ "armor_class": 5 })

    combat = Combat(c, defn)
    
    prevXP = c.xp
    prevLevel = c.level
    result = combat.resolve(roll)

    assert c.level == prevLevel + 1 and c.xp == prevXP + 10
