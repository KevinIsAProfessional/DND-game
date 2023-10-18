import Roll
import Character


class Combat:
    """Runs an entire combat"""

    def __init__(self, combatants):
        self.order = roll_for_initiative(combatants)

    def get_combat_order(self):
        for char in self.order:
            print(char[1].name)


def roll_for_initiative(combatants):
    """Assigns an initiative roll to each character in a list of characters"""
    order = []
    for character in combatants:
        order.append((Roll.roll("d20", 1), character))
    return sorted(order, key=lambda pair: pair[0])


def attack(attacker: Character, defender: Character):
    print(
        f"{attacker.get_name()} swings their {attacker.get_equipped_items()[0]} at {defender.get_name()}")
    attack_roll = Roll.roll("d20", 1)[0]
    print(f"Rolling...... {attack_roll}!")
    if attack_roll >= defender.get_ac():
        damage = attacker.damage()
        print(f"Hit! {defender.get_name()} takes {damage} points of damage.")
        defender.take_damage(damage)
    else:
        print("Missed!")
