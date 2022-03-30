from evercraft.utils.property import EvercraftProperty
from evercraft.models.character import Character

class Combat():
    attacker = Character()
    defender = Character()

    DAMAGE = 1
    CRITICAL_HIT = 2

    def __init__(self, attacker = attacker, defender = defender):
        self.attacker = attacker
        self.defender = defender

    def resolve(self, roll):
        if roll == 20:
            self.defender.hit_points = self.defender.hit_points - self.CRITICAL_HIT
        
        elif roll >= self.defender.armor_class:
            self.defender.hit_points = self.defender.hit_points - self.DAMAGE

        else:
            return "missed me!"

        