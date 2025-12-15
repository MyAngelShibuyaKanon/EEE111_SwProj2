from enum import Enum
from types import NoneType


class CharacterType(Enum):
    FIRE = ("FIRE", "WATER", "EARTH")
    EARTH = ("EARTH", "FIRE", "WATER")
    WATER = ("WATER", "WATER", "FIRE")
    LIGHT = ("LIGHT", None, "DARK")
    DARK = ("FIRE", None, "LIGHT")

    def __init__(self, typeName: str, weakness: str | NoneType, strength: str) -> None:
        self.typeName = typeName
        self.weakness = weakness
        self.strength = strength
        pass
