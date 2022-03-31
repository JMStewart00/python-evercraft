from enum import Enum
from evercraft.utils.property import EvercraftProperty, DefaultProperty

class AbilityType(Enum):
    STRENGTH = 0
    DEXTERITY = 1
    CONSTITUTION = 2
    WISDOM = 3
    INTELLIGENCE = 4
    CHARISMA = 5

class Ability():
    score = DefaultProperty(10)
    mod = DefaultProperty(0)
    SCORE_MODS = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 5,
    }

    def __init__(self, ab_type):
        self.ab_type = ab_type
        self.score = self.score
        self.mod = self.mod

    def adjust_score_and_mod(self, score):
        self.score = score
        self.mod = self.SCORE_MODS.get(score)

    def __repr__(self):
        name = self.ab_type
        score = self.score
        mod = self.mod
        return '{}, Score {}, Mod {}'.format(name, score, mod)