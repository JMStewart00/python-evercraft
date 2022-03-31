import pytest
from evercraft.models.character import Character
from evercraft.models.combat import Combat

def test_character_is_alive():
    c = Character()
    assert c.is_dead() == False

def test_character_is_alive_after_single_attack():
    roll = 15
    att = Character()
    defn = Character()

    combat = Combat(att, defn)
    result = combat.resolve(roll)
    assert defn.is_dead() == False

def test_character_can_die_after_single_attack():
    roll = 20
    att = Character()
    defn = Character({ "hit_points": 2 })

    combat = Combat(att, defn)
    result = combat.resolve(roll)
    assert defn.is_dead() == True

def test_character_is_dead_after_multiple_attacks():
    att = Character()
    defn = Character()
    roll = 18

    while defn.hit_points > 0:
        combat = Combat(att, defn)
        combat.resolve(roll)

    assert defn.is_dead() == True

