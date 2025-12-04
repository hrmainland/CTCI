# My solution to p06_towers_of_hanoi.py
"""
[5, 4, 3, 2, 1]
[]
[]

hanoi(stacks)

move(depth, occ, target)

spare = not occ or target

- move(depth - 1, occ, spare)
- single_move(occ, target)
- move(depth - 1, spare, target)


[]
[2, 1]
[3]
"""


def hanoi(stacks):
    def rec_move(depth, occ, target):
        print(stacks)
        spare = 3 - (occ + target)
        if depth == 0:
            return
        rec_move(depth - 1, occ, spare)
        move_sinlge(occ, target)
        rec_move(depth - 1, spare, target)

    def move_sinlge(occ, target):
        stacks[target].append(stacks[occ].pop())

    rec_move(len(stacks[0]), 0, 2)
    return stacks


stacks = [[5, 4, 3, 2, 1], [], []]

print(hanoi(stacks))
