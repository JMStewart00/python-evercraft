from evercraft.utils.property import EvercraftProperty
from evercraft.models.character import Character
from evercraft.models.ability import AbilityType

from math import floor

class Combat():
    attacker = Character()
    defender = Character()

    DAMAGE = 1
    CRITICAL_HIT_MULTIPLIER = 2

    def __init__(self, attacker = attacker, defender = defender):
        self.attacker = attacker
        self.defender = defender

    def resolve(self, roll):
        print("ROLL {}\n".format(roll))

        strength_index = AbilityType.STRENGTH.value
        calculated_roll = self.attacker.abilities[strength_index].mod + roll
        calculated_hit = self.attacker.abilities[strength_index].mod + self.attacker.hit_points + floor(self.attacker.level / 2)
        damage = calculated_hit if calculated_hit >= 1 else 1

        print("Attacker:")
        print("STRENGTH {}\nCALC ROLL {}\nCALC HIT {}\nMOD HIT {}\n".format(self.attacker.abilities[strength_index].score,roll,calculated_roll,calculated_hit,damage))



        hit_landed = False
        current_defn_hp = self.defender.hit_points
        dex_index = AbilityType.DEXTERITY.value
        current_defn_armor = self.defender.armor_class + self.defender.abilities[dex_index].mod
        print("===============\n")
        print("Defender:")
        print("ARMOR {}\nHP {}\nDAMAGE {}\n".format(self.defender.armor_class,current_defn_hp,damage))
        if roll == 20:
            print("**** CRITICAL HIT ****\n\n\n")
            hit_landed = True
            self.defender.hit_points = current_defn_hp - (self.CRITICAL_HIT_MULTIPLIER * damage)
        
        elif calculated_roll >= current_defn_armor:
            print("**** HIT LANDED ****\n\n\n")
            hit_landed = True
            self.defender.hit_points = current_defn_hp - damage

        else:
            print("**** MISSED ****\n\n\n")
            return "**** MISSED ****"

        if hit_landed:
            self.attacker.recalculate()

        print("Defender HP Remaining {}\n".format(self.defender.hit_points))
        print("Defender is DEAD {}\n".format(self.defender.is_dead()))

        