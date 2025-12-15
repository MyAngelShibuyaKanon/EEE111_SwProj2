from dataclasses import asdict

from core.character import Character
from core.characterInfo import CharacterInfo
from core.characterTypes import CharacterType
from features.actions.normalAttack import NormalAttack
from features.actions.typeAttack import TypeAttack
from features.effects.effects import Effect


class Game:
    def start(self):
        """
        Starts the "Game"/ DMG calculator
        """
        # Initialize actions
        normalAttack = NormalAttack()
        typeAttack = TypeAttack()

        # Initialize 2 chatacters, dict is used to store character info and is unpacked to
        # be passed as an argument
        print("### Attacker Setup ###")
        attacker = Character(**self.getCharInfo(isAttacker=True))
        print("### Target Setup ###")
        target = Character(**self.getCharInfo(askEvade=True, isAttacker=False))

        # Simple attack flow using if-else
        print("### Choose Attack ###")
        if self.isAttackNormal("Attack Type (Normal/Type): "):
            dmgString = normalAttack.execute(attacker, target)
        else:
            dmgString = typeAttack.execute(attacker, target)
        print(dmgString)
        print(f"{target.name}'s HP after attack: {target.totalHp}")
        pass

    def getCharInfo(self, isAttacker: bool, askEvade: bool = False) -> dict:
        """
        Obtains character info by storing it in a dataclass CharacterInfo and returning
        it as a dictionary. I love dataclasses.
        """
        charInfo = CharacterInfo()
        charInfo.name = input(f"{'Attacker' if isAttacker else 'Target'} Name: ")
        charInfo.HP = self.getInt("HP: ")
        charInfo.ATK = self.getInt("ATK: ")
        charInfo.DEF = self.getInt("DEF: ")
        charInfo.charType = self.getType()
        charInfo.weaponAtk = self.getInt("Weapon ATK bonus: ")
        charInfo.armorDef = self.getInt("Armor DEF bonus: ")
        print(f"Applying {'Buffs' if isAttacker else 'Debuffs'} (50%)")
        charInfo.buffs, charInfo.debuffs = self.getEffects(askEvade=askEvade)

        return asdict(charInfo)

    def getType(self) -> CharacterType:
        """
        Gets CharacterType (Fire, Earth, etc) from input() in a error-handled way and returns
        it with the correct type
        """
        while True:
            try:
                return CharacterType[
                    input("Type(Fire/Earth/Water/Light/Dark): ").upper()
                ]  # This gets the correct type object from the CharacterType ENUM
            except:
                print("Invalid character type!")

    def getBool(self, string: str) -> bool:
        """
        Gets Bool from input() through y/n and returns
        it with the correct type
        """
        while True:
            match input(string).lower():
                case "y":
                    return True
                case "n":
                    return False
                case _:
                    print("Invalid input")

    def isAttackNormal(self, string: str) -> bool:
        """
        Gets Bool through input() and returns
        it with the correct type
        """
        while True:
            match input(string).lower():
                case "normal":
                    return True
                case "type":
                    return False
                case _:
                    print("Invalid input")

    def getInt(self, string: str) -> int:
        """
        Gets int from input() and returns it
        with the correct type
        """
        while True:
            try:
                return int(input(string))
            except:
                print("Input not an int")

    def getEffects(self, askEvade: bool) -> tuple[list[Effect], list[Effect]]:
        """
        Gets list of buffs and effects through a series of getBools,
        asking if a certain buff/debuff should be added. returns list of buff and
        list of debuffs wrapped in tuple
        """
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
