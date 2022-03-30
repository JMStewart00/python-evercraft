from evercraft.utils.property import EvercraftProperty
from evercraft.models.ability import Ability, AbilityType

class Alignment():
    GOOD, NEUTRAL, EVIL = range(3)

class Character():
    DEFAULT_ATTR = {
        "abilities": [],
        "alignment": Alignment.NEUTRAL,
        "armor_class": 10,
        "hit_points": 5,
        "name": "Unnamed Character",
    }

    abilities = EvercraftProperty()
    alignment = EvercraftProperty()
    armor_class = EvercraftProperty()
    hit_points = EvercraftProperty()
    name = EvercraftProperty()

    def __init__(self, obj = None):
        if not isinstance(obj, dict) and obj is not None:
            raise ValueError("Sorry, you need to pass an object in to Character creation.")

        # Loop through the default attributes to check if
        # there are values in need of update
        for key in self.DEFAULT_ATTR:
            if obj and key in obj.keys():
                value = obj[key]
            else:
                value = self.DEFAULT_ATTR[key]

            setattr(self, key, value)

        # initialize the abilities with default values
        for i in AbilityType:
            ability = Ability(i)
            self.abilities.append(ability)

    # returns a str representation of the Character in the str() method.
    def __str__(self):
        return self.name

    def is_dead(self):
        return False if self.hit_points > 0 else True
