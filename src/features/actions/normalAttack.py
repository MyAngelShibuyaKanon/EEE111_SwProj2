from core.character import Character
from features.actions.action import Action


class NormalAttack(Action):
    def execute(self, attacker: Character, target: Character):
        # Get damage by subtracting target's total def to attakcer's total attack
        DMG: int = attacker.totalAtk - target.totalDef

        # Apply evasion multiplier if evade buff is enabled
        if target.applyEvade:
            DMG = int(DMG * 0.25)

        # Ensure minimum dmg is 1
        DMG = DMG if DMG > 0 else 1

        # Sets target's hp to target's total hp - damage divided by the target's hp multiplier
        # this is done to ensure that when calling target's total hp which relies on base hp
        # the totalHp will be the correct value. sets minimum hp value to 0
        target.HP = (
            (target.totalHp - DMG) / target.hpMult if (target.totalHp - DMG) >= 0 else 0
        )

        dmgString = f"{attacker.name} deals {DMG} {'(miss) ' if target.applyEvade else ''}damage to {target.name}!"
        return dmgString
