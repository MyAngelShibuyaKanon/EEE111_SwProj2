from abc import ABC, abstractmethod
from core.character import Character


class Action(ABC):
    """
    Interface for the two attack methods
    """

    @abstractmethod
    def execute(self, attacker: Character, target: Character) -> str:
        """
        Executes an attack from attacker to target
        """
        pass
