"""
"aabc"

{a:2, b:1, c:1}

"""

from collections import Counter


def perms(string):
    freq = Counter(string)
    result = []

    def recurse(index, prefix):
        if index == len(string):
            result.append(prefix)
        for char, count in freq.items():
            if count == 0:
                continue
            freq[char] -= 1
            recurse(index + 1, prefix + char)
            # backtrack
            freq[char] += 1

    recurse(0, "")
    return result


string = "aabc"
result = perms(string)
print(result)
