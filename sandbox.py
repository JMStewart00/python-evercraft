from evercraft.models.combat import Combat
from evercraft.models.character import Character, Alignment
from evercraft.models.ability import Ability, AbilityType
from evercraft.utils.property import DefaultProperty
from random import randint
from math import floor

char = {
    "name": "Thor",
}
att = Character(char, STRENGTH=17)

for i in range(0,500):
    roll = randint(1, 20)
    defn = Character()
    combat = Combat(att, defn)
    result = combat.resolve(roll)

print(att)

