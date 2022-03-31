from evercraft.utils.property import EvercraftProperty
from evercraft.models.ability import Ability, AbilityType
from math import floor

class Alignment():
    GOOD, NEUTRAL, EVIL = range(3)

class Character():
    DEFAULT_ATTR = {
        "abilities": [],
        "alignment": Alignment.NEUTRAL,
        "armor_class": 10,
        "hit_points": 5,
        "level": 1,
        "name": "Unnamed Character",
        "xp": 0,
    }

    ATTACK_SUCCESS_HP = 10

    abilities = EvercraftProperty()
    alignment = EvercraftProperty()
    armor_class = EvercraftProperty()
    hit_points = EvercraftProperty()
    level = EvercraftProperty()
    name = EvercraftProperty()
    xp = EvercraftProperty()

    def __init__(self, obj = None, **abilities):
        if not isinstance(obj, dict) and obj is not None:
            raise ValueError("Sorry, you need to pass an object in to Character creation.")

        for item in abilities.values():
            if not isinstance(item, int) or item not in range(1,21):
                raise ValueError("Sorry! Character ability scores need to be an INT between 1 and 20")

        # Loop through the default attributes to check if
        # there are values in need of update
        for key in self.DEFAULT_ATTR:
            if obj and key in obj.keys():
                value = obj[key]
            else:
                value = self.DEFAULT_ATTR[key]

            setattr(self, key, value)

        self.set_abilities(abilities)

    # returns a str representation of the Character in the str() method.
    def __str__(self):
        return " Name {} \n HP {} \n Lvl {} \n XP {} \n".format(self.name, self.hit_points, self.level, self.xp)

    def is_dead(self):
        return False if self.hit_points > 0 else True

    def set_abilities(self, kwargs):
        # initialize the abilities with default values
        for i in AbilityType:
            ability = Ability(i)
            self.abilities.append(ability)

        # If values were passed to in other than defaults,
        # update those too
        if kwargs is not None:
            for ab in self.abilities:
                index = ab.ab_type.value
                lookup = self.find_ability(index)
                name = lookup.ab_type.name
                if name in kwargs:
                    score = kwargs[name]
                    self.update_ability(index, score)
    
    def find_ability(self, index):
        return self.abilities[index]

    def update_ability(self, index, score):
        a = self.find_ability(index)
        a.adjust_score_and_mod(score)

    def recalculate(self):
        self.xp_gained()
        is_level_up = self.check_level_up()
        if is_level_up:
            self.level_up()
        
    def xp_gained(self):
        self.xp += self.ATTACK_SUCCESS_HP

    def check_level_up(self):
        if self.level != floor(self.xp / 1000):
            return True
        else: 
            return False

    def level_up(self):
        self.level = floor(self.xp / 1000)

        con_index = AbilityType.CONSTITUTION.value
        self.hit_points += 5 + self.abilities[con_index].mod

class Rogue(Character):
    pass
class Paladin(Character):
    pass
class Monk(Character):
    pass
class Fighter(Character):
    pass