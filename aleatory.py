#!/usr/bin/python3
"""
import random

members = ["luz", "Leo", "niña", "kiki", "saki"]
leader = random.choice(members)
print(leader)
"""

import random


class Dice:

    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return(first, second)

dice = Dice()
print(dice.roll())
