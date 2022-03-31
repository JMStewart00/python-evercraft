import pytest
from evercraft.models.character import Character
from evercraft.models.combat import Combat

# As a combatant I want to be able to attack other combatants so that I can survive to fight another day

# roll a 20 sided die (don't code the die)
# roll must meet or beat opponents armor class to hit
# a natural roll of 20 always hits
def test_can_create_combat():
    combat = Combat()
    assert isinstance(combat, Combat)

def test_characters_combat_involves_two_characters():
    attacker = Character()
    defender = Character()
    fight = Combat(attacker, defender)
    assert isinstance(fight.attacker, Character) and isinstance(fight.defender, Character)

def test_combat_has_resolution_method():
    assert hasattr(Combat, 'resolve') and callable(getattr(Combat, 'resolve'))


# As an attacker I want to be able to damage my enemies so that they will die and I will live

# If attack is successful, other character takes 1 point of damage when hit
# If a roll is a natural 20 then a critical hit is dealt and the damage is doubled
# when hit points are 0 or fewer, the character is dead
def test_combat_resolution_accounts_for_20_on_die():
    roll = 20
    att = Character()
    defn = Character({ "armor_class": 10 })

    combat = Combat(att, defn)
    prevHP = defn.hit_points
    result = combat.resolve(roll)
    assert defn.hit_points == (prevHP - Combat.CRITICAL_HIT_MULTIPLIER)

def test_combat_resolution_for_meet_or_beat_opponent_armor():
    roll = 10
    att = Character()
    defn = Character({ "armor_class": 10 })

    combat = Combat(att, defn)
    prevHP = defn.hit_points
    result = combat.resolve(roll)
    assert defn.hit_points == (prevHP - Combat.DAMAGE)

def test_combat_resolution_for_less_than_opponent_armor():
    roll = 10
    att = Character()
    defn = Character({ "armor_class": 11 })

    combat = Combat(att, defn)
    result = combat.resolve(roll)
    assert result == "**** MISSED ****"
