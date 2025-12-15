from core.character import Character
from features.actions.action import Action


class NormalAttack(Action):
    def execute(self, attacker: Character, target: Character):
        DMG: int = attacker.totalAtk - target.totalDef
        if target.applyEvade:
            DMG = int(DMG * 0.25)
        DMG = DMG if DMG > 0 else 1
        target.HP = (
            (target.totalHp - DMG) / target.hpMult if (target.totalHp - DMG) >= 0 else 0
        )

        dmgString = f"{attacker.name} deals {DMG} {'(miss) ' if target.applyEvade else ''}damage to {target.name}!"
        return dmgString
