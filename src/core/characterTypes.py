from enum import Enum
from types import NoneType


class CharacterType(Enum):
    """
    Enum of CharacterType
    """

    FIRE = ("FIRE", "WATER", "EARTH")
    EARTH = ("EARTH", "FIRE", "WATER")
    WATER = ("WATER", "EARTH", "FIRE")
    LIGHT = ("LIGHT", None, "DARK")
    DARK = ("DARK", None, "LIGHT")

    def __init__(self, typeName: str, weakness: str | NoneType, strength: str) -> None:
        self.typeName = typeName
        self.weakness = weakness
        self.strength = strength
        pass
