import pytest
from random import randint

from evercraft.models.character import Character
from evercraft.models.ability import Ability, AbilityType
from evercraft.models.combat import Combat

def test_character_can_set_xp():
    xp = 20
    c = Character()
    c.xp = xp
    assert c.xp == xp

def test_character_gains_xp_after_hit():
    roll = 10
    att = Character()
    defn = Character({ "armor_class": 5 })

    combat = Combat(att, defn)
    
    prevXP = att.xp
    result = combat.resolve(roll)
    assert att.xp > prevXP

def test_character_gains_10_xp_after_hit():
    roll = 19
    att = Character()
    defn = Character({ "armor_class": 5 })

    combat = Combat(att, defn)
    
    prevXP = att.xp
    result = combat.resolve(roll)
    assert att.xp == (prevXP + 10)