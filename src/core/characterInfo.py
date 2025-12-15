from dataclasses import dataclass
from typing import Optional
from core.characterTypes import CharacterType
from features.effects.effects import Effect


@dataclass
class CharacterInfo:
    name: Optional[str] = None
    HP: Optional[int] = None
    ATK: Optional[int] = None
    DEF: Optional[int] = None
    charType: Optional[CharacterType] = None
    weaponAtk: Optional[int] = None
    armorDef: Optional[int] = None
    buffs: Optional[list[Effect]] = None
    debuffs: Optional[list[Effect]] = None
    applyEvade: bool = False
