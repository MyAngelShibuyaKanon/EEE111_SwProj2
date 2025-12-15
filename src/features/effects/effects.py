from enum import Enum


class Stat(Enum):
    """
    Enum of Stat
    """

    HP = "HP"
    ATK = "ATK"
    DEF = "DEF"
    EVADE = "EVADE"


class Effect(Enum):
    """
    Enum of effect (buffs and debuffs). Each effect contains the affected stat and
    the multiplier applied to that stat. Merge of buff and debuffs into one class
    """

    HP_BUFF = (Stat.HP, 1.5)
    ATK_BUFF = (Stat.ATK, 1.5)
    DEF_BUFF = (Stat.DEF, 1.5)
    HP_DEBUFF = (Stat.HP, 0.5)
    ATK_DEBUFF = (Stat.ATK, 0.5)
    DEF_DEBUFF = (Stat.DEF, 0.5)
    EVADE_BUFF = (Stat.EVADE, 1)

    def __init__(self, affectedStat, multiplier) -> None:
        self.affectedStat = affectedStat
        self.multiplier = multiplier
