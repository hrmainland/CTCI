# My solution to p01_insertion.py


def bits(x, n=8):
    return format(x & ((1 << n) - 1), f"0{n}b")


left = -1 << 4
right = (1 << 3) - 1

print(bin(left), bin(right))

mask = left | right

print(bits(mask))


print(bits(-3))


print(bin(0.34))
