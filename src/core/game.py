from dataclasses import asdict

from core.character import Character
from core.characterInfo import CharacterInfo
from core.characterTypes import CharacterType
from features.actions.normalAttack import NormalAttack
from features.actions.typeAttack import TypeAttack
from features.effects.effects import Effect


class Game:
    def start(self):
        normalAttack = NormalAttack()
        typeAttack = TypeAttack()
        print("### Attacker Setup ###")
        attacker = Character(**self.getCharInfo(isAttacker=True))
        print("### Target Setup ###")
        target = Character(**self.getCharInfo(askEvade=True, isAttacker=False))
        print("### Choose Attack ###")
        if self.isAttackNormal("Attack Type (Normal/Type): "):
            dmgString = normalAttack.execute(attacker, target)
        else:
            dmgString = typeAttack.execute(attacker, target)
        print(dmgString)
        print(f"{target.name}'s HP after attack: {target.totalHp}")
        pass

    def getCharInfo(self, isAttacker: bool, askEvade: bool = False) -> dict:
        charInfo = CharacterInfo()
        charInfo.name = input(f"{'Attacker' if isAttacker else 'Target'} Name: ")
        charInfo.HP = int(input("HP: "))
        charInfo.ATK = int(input("ATK: "))
        charInfo.DEF = int(input("DEF: "))
        charInfo.charType = self.getType()
        charInfo.weaponAtk = int(input("Weapon ATK bonus: "))
        charInfo.armorDef = int(input("Armor DEF bonus: "))
        print(f"Applying {'Buffs' if isAttacker else 'Debuffs'} (50%)")
        charInfo.buffs, charInfo.debuffs = self.getEffects(askEvade=askEvade)

        return asdict(charInfo)

    def getType(self) -> CharacterType:
        while True:
            try:
                return CharacterType[
                    input("Type(Fire/Earth/Water/Light/Dark): ").upper()
                ]
            except:
                print("Invalid character type!")

    def getBool(self, string: str) -> bool:
        while True:
            match input(string).lower():
                case "y":
                    return True
                case "n":
                    return False
                case _:
                    print("Invalid input")

    def isAttackNormal(self, string: str) -> bool:
        while True:
            match input(string).lower():
                case "normal":
                    return True
                case "type":
                    return False
                case _:
                    print("Invalid input")

    def getInt(self, string: str) -> int:
        while True:
            try:
                return int(input(string))
            except:
                print("Input not an int")

    def getEffects(self, askEvade: bool) -> tuple[list[Effect], list[Effect]]:
        buffs: list[Effect] = []
        debuffs: list[Effect] = []
        if self.getBool("Apply HP Buff? (y/n): "):
            buffs.append(Effect.HP_BUFF)
        if self.getBool("Apply ATK Buff? (y/n): "):
            buffs.append(Effect.ATK_BUFF)
        if self.getBool("Apply DEF Buff? (y/n): "):
            buffs.append(Effect.DEF_BUFF)
        if askEvade and self.getBool("Apply EVASION Buff? (y/n): "):
            buffs.append(Effect.EVADE_BUFF)
        if self.getBool("Apply HP Debuff? (y/n): "):
            debuffs.append(Effect.HP_DEBUFF)
        if self.getBool("Apply ATK Debuff? (y/n): "):
            debuffs.append(Effect.ATK_DEBUFF)
        if self.getBool("Apply DEF Debuff? (y/n): "):
            debuffs.append(Effect.DEF_DEBUFF)
        return (buffs, debuffs)
