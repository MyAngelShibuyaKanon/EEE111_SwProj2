from core.character import Character
from features.actions.action import Action


class TypeAttack(Action):
    def execute(self, attacker: Character, target: Character):
        if attacker.charType.strength == target.charType.name:
            multiplier = 1.5
        elif attacker.charType.weakness == target.charType.name:
            multiplier = 0.5
        else:
            multiplier = 1
        DMG: int = int((attacker.totalAtk - target.totalDef) * multiplier)
        if target.applyEvade:
            DMG = int(DMG * 0.25)
        DMG = DMG if DMG > 0 else 1
        target.HP = (
            (target.totalHp - DMG) / target.hpMult if (target.totalHp - DMG) >= 0 else 0
        )
        dmgString = f"{attacker.name} deals {DMG} {'(miss) ' if target.applyEvade else ''}damage to {target.name}!"
        return dmgString
