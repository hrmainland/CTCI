# My solution to p09_bst_sequences.py
from tree import *
from itertools import combinations, permutations, product

# for elem in product(range(5), repeat=2):
#     print(elem)

def get_inserts(len):
    result = []
    for i in range(len):
        for j in range (i, len):
            result
            

def weave(string_1, string_2):
    result = []
    spots = range(len(string_1) + 1)
    inserts = product(spots, repeat=len(string_2))
    print(list(inserts))
    for insert in inserts:
        this_list = list(string_1)
        for j in reversed(range(len(string_2))):
            this_list.insert(insert[j], string_2[j])
        result.append("".join(this_list))
    return result


results = weave("ab", "xy")
for result in results:
    print(result)
