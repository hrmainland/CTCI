# My solution to p01_triple_step.py
def n_ways_bu(n):
    if n < 4:
        return n
    a, b, c = 1, 2, 4
    for i in range(4, n):
        d = a + b + c
        a, b, c = b, c, d
    return a + b + c


print(n_ways_bu(4))
