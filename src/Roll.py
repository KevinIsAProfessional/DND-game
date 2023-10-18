import random


def roll(dice: str, number: int) -> []:
    die = {"d4": 4,
           "d6": 6,
           "d8": 8,
           "d10": 10,
           "d12": 12,
           "d20": 20,
           "d100": 100}[dice]

    results = []
    for _ in range(number):
        results.append(random.randint(1, die))
    return results
