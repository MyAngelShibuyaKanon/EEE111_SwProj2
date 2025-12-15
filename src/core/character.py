from typing import List

from core.characterTypes import CharacterType
from features.effects.effects import Effect, Stat
from features.equipment.armor import Armor
from features.equipment.weapon import Weapon


class Character:
    """
    Main character class for Attacker and Target
    """

    def __init__(
        self,
        name: str,
        HP: float,
        ATK: int,
        DEF: int,
        charType: CharacterType,
        weaponAtk: int,
        armorDef: int,
        buffs: List[Effect],
        debuffs: List[Effect],
        applyEvade: bool,
    ) -> None:
        # Initialize name, stats, and CharacterType
        self.name = name
        self.HP = HP
        self.hpMult = 1
        self.ATK = ATK
        self.atkMult = 1
        self.DEF = DEF
        self.defMult = 1
        self.charType = charType

        # Initialize weapons and armor by instantiating with equipmentStats from params
        self.weapon: Weapon = Weapon(weaponAtk)
        self.armor: Armor = Armor(armorDef)

        # Set buffs/debuffs and apply them
        self.buffs = buffs
        self.debuffs = debuffs
        self.applyEvade = applyEvade
        self.applyEffects(self.buffs)
        self.applyEffects(self.debuffs)

    @property
    def totalHp(self) -> int:
        """
        Returns total HP of the character (baseHp + (de)buffs)
        """
        return round((self.HP * self.hpMult))

    @property
    def totalAtk(self) -> int:
        """
        Returns total attack stat of the character (baseAtk + weapon + (de)buffs)
        """
        return int((self.ATK + self.weapon.atkBonus) * self.atkMult)

    @property
    def totalDef(self) -> int:
        """
        Returns total DEF of the character (baseDef + armor + (de)buffs)
        """
        return int((self.DEF + self.armor.defBonus) * self.defMult)

    def applyEffects(self, effects: List[Effect]):
        """
        Apply the effects in the passed param "effects" through recursion
        acceps list of Effect
        """
        # Base case
        if not effects:
            return

        # Recursive step
        else:
            effect = effects[0]
            match effect.affectedStat:
                case Stat.HP:
                    self.hpMult *= effect.multiplier
                case Stat.ATK:
                    self.atkMult *= effect.multiplier
                case Stat.DEF:
                    self.defMult *= effect.multiplier
                case Stat.EVADE:
                    self.applyEvade = True

            return effects[1:]  # call same function with the processed effect removed
