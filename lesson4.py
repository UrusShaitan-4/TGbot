# Завдання 1
# Створіть абстрактний клас Character, атрибути
#  name – ім’я
#  max_hp – максимальний рівень здоров’я
#  hp – нинішній рівень здоров’я
#  level – рівень персонажа(від 1 до 20)
#  intelligence – стат інтелекту
#  strength – стат сили
#  dexterity – стат спритності
#  mana – стат мани
#  defense – стат захисту
# Методи:
#  attack() – абстрактний метод
#  take_damage(damage) – отримує урон, зменшений на
# захист
#  level_up() – збільшує рівень
#  increase_stat(stat) – збільшує один з статів на 1
#  rest() – відпочинок(відновлює hp до максимального)
#  heal(heal_hp) – збільшує hp на heal_hp
from abc import ABC, abstractmethod
from enum import Enum


class Stat(Enum):
    intelligence = "intelligence"
    strength = "strength"
    dexterity = "dexterity"
    mana = "mana"
    defense = "defense"


class Character(ABC):
    def __init__(self,
                 name:str,
                 max_hp:int,
                 intelligence:int,
                 strength:int,
                 dexterity:int,
                 mana:int,
                 defense:int,
                 level: int = 1,
                 ):

        self._name = name
        self._max_hp = max_hp
        self._level = level
        self._hp = max_hp
        self._intelligence = intelligence
        self._strength = strength
        self._dexterity = dexterity
        self._mana = mana
        self._defense = defense

    @abstractmethod
    def attack(self)->int:
        pass

    def take_damage(self, damage:int):
        damage -= self._defense

        if damage > 0:
            self._hp -= damage

    def level_up(self):
        if self._level < 20:
            self._level +=1

    def increase_stat(self, stat:Stat):
        if stat == Stat.intelligence:
            self._intelligence += 1
        elif stat == Stat.strength:
            self._strength += 1
        elif stat == Stat.dexterity:
            self._dexterity += 1
        elif stat == Stat.defense:
            self._defense += 1
        elif stat == Stat.mana:
            self._mana += 1

    def rest(self):
        self._hp = self._max_hp

    def heal(self,heal_hp:int):
        if heal_hp > 0:
            self._hp += heal_hp

        if self._hp > self._max_hp:
            self._hp = self._max_hp


# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana

class Paladin(Character):

    def attack(self) -> int:
        if self._mana >= 5:
            self._mana -= 5
            return 4*self._strength
        return self._strength

    def shield(self):
        self._defense += self._level+4

    def unshield(self):
        self._defense -= 4+self._level

    def  heal_ally(self, ally:Character):
        heal_amount = 5 + 2 * self._level + 0.5 * self._mana
        ally.heal(int(heal_amount))


# Завдання 3
# Створіть дочірній клас Mage
# Методи:
#  attack() – наносить 3*intelligence+4 урону та зменшує
# mana на 3, якщо недостатньо, то не наносить урону
#  fireball() – наносить 2*intelligence+3 урону по області та
# зменшує mana на 5, якщо недостатньо, то не наносить
# урону
#  heal_ally(ally) – лікує союзника на 3 + level +
# 3*intelligence




char = Paladin("Paladin", 100, 30,20,10,100,40)
ally = Paladin("Ally", 100, 20,30,20,100,20)

char.level_up()
char.shield()
ally.shield()
ally.take_damage(80)
print(ally._hp)
char.heal_ally(ally)
print(ally._hp)


