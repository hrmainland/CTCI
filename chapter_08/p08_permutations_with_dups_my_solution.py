# My solution to p07_permutations_without_dups.py

"""


options = [a, b, c]

a

ab
ba

result

rec(used_idx):
    #base base
    if len(used_idx)
    for every non-used index:
        used_idx += index
        rec(used_idx, word + new char)
        used_idx.pop()

result = []
used_idx = {}
word = ""

"ab"


"""


def perms(string):
    result = []

    def recurse(used_idx, word):
        # base case
        if len(used_idx) == len(string):
            result.append(word)
            return
        # main body
        for i in range(len(string)):
            if i not in used_idx:
                used_idx.add(i)
                recurse(used_idx, word + string[i])
                used_idx.remove(i)

    recurse(set(), "")
    return result


def perms_2(string):
    if len(string) == 0:
        return [""]
    first_char = string[0]
    post_perms = perms_2(string[1:])
    for perm in post_perms:
        for i in range(len(perm) + 1):
            new = perm[:i] + first_char + perm[i:]
            post_perms.append(new)
    return post_perms


string = "abcd"
print(perms_2(string))
