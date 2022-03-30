from enum import Enum
from evercraft.utils.property import EvercraftProperty

class AbilityType(Enum):
    STRENGTH = 1
    DEXTERITY = 2
    CONSTITUTION = 3
    WISDOM = 4
    INTELLIGENCE = 5
    CHARISMA = 6

class Ability():
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
        self.score = 10
        self.mod = 0

    def update_attributes(self, score):
        self.score = score
        self.mod = self.SCORE_MODS.get(score)

    

    