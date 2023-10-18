import random


class Character:
    def __init__(self, name="Anon", max_hp=10, current_hp=10, ac=10, equipped_items=None):
        self.name = name
        self.max_hp = max_hp
        self.hp = current_hp
        self.ac = ac
        self.equipped_items = equipped_items
        self.damage = lambda: random.randint(1, 8)
        if self.max_hp < self.hp:
            self.hp = self.max_hp

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_ac(self):
        return self.ac

    def get_equipped_items(self):
        return self.equipped_items

    def take_damage(self, amount):
        self.hp -= amount
        self.check_condition()

    def check_condition(self):
        health_percentage = self.hp / self.max_hp
        if health_percentage <= 0:
            print(f"{self.name} is unconscious")
        elif health_percentage < .5:
            print(f"{self.name} is bloodied")
