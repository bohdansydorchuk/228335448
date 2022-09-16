"""Фантастическая битва"""

import random
from oop_module import armor_list, long_range_weapons,human_names, close_combat_weapons

class Warrior:
    def __init__(self):
        self.name = random.choice(human_names)
        self.health = random.randint(60, 80)
        self.weapon = random.choice(close_combat_weapons)
        self.attack_power = random.randint(5, 40)
        self.armor = random.choice(armor_list)
        self.armor_class = random.randint(10, 20)

class Archer:
    def __init__(self):
        self.name = random.choice(human_names)
        self.health = random.randint(40, 70)
        self.weapon = random.choice(long_range_weapons)
        self.attack_power = random.randint(40, 80)
        self.armor = random.choice(armor_list)
        self.armor_class = random.randint(2, 6)

class Defender:
    def __init__(self):
        self.name = random.choice(human_names)
        self.health = 100
        self.weapon = random.choice(close_combat_weapons)
        self.attack_power = 50
        self.armor = random.choice(armor_list)
        self.armor_class = 10