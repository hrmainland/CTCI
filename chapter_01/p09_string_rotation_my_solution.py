# My solution to p09_string_rotation.py


def check(s1, s2, s2_index):
    for i in range(len(s1)):
        if s1[i] != s2[s2_index + i]:
            return False
    return True


def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(-len(s2), -1):
        if check(s1, s2, i):
            return True
    return False


print(string_rotation("waterbottle", "bottlewater"))
