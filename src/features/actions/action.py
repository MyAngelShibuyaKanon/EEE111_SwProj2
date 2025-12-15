from abc import ABC, abstractmethod
from core.character import Character


class Action(ABC):
    @abstractmethod
    def execute(self, attacker: Character, target: Character) -> str:
        pass
