# My solution to p04_next_number.py
import math


def lower(num):
    if math.log(num + 1, 2) % 1 == 0:
        return None
    mask = 3
    i = 1
    while mask & num != (1 << i):
        mask = mask << 1
        i += 1
    return num - (1 << i) + (1 << (i - 1))


def higher(num):
    if math.log(num + 1, 2) % 1 == 0:
        return None
    mask = 3
    i = 0
    while mask & num != (1 << i):
        mask = mask << 1
        i += 1
    return num + (1 << (i + 1)) - (1 << i)



print(higher(11))
