from typing import List

from core.characterTypes import CharacterType
from features.effects.effects import Effect, Stat
from features.equipment.armor import Armor
from features.equipment.weapon import Weapon


class Character:
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
        self.name = name
        self.HP = HP
        self.hpMult = 1
        self.ATK = ATK
        self.atkMult = 1
        self.DEF = DEF
        self.defMult = 1
        self.charType = charType
        self.weapon: Weapon = Weapon(weaponAtk)
        self.armor: Armor = Armor(armorDef)
        self.buffs = buffs
        self.debuffs = debuffs
        self.applyEvade = applyEvade
        self.applyEffects(self.buffs)
        self.applyEffects(self.debuffs)

    @property
    def totalHp(self) -> int:
        return round((self.HP * self.hpMult))

    @property
    def totalAtk(self) -> int:
        return int((self.ATK + self.weapon.atkBonus) * self.atkMult)

    @property
    def totalDef(self) -> int:
        return int((self.DEF + self.armor.defBonus) * self.defMult)

    def applyEffects(self, effects: List[Effect]):
        if not effects:
            return
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

            return effects[1:]
