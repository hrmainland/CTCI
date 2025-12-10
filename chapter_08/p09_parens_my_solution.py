"""

{"(": 3, ")": 3}

try both



1: ()
2: ()(), (())
3: ()()(), (()()), (())(), ()(()), ((())),
"""


def all_valid(n):
    result = []
    freq = {"(": n, ")": n}

    def is_balanced():
        return freq["("] == freq[")"]

    def rec_search(prefix):
        # base case
        if len(prefix) == 2 * n:
            result.append(prefix)

        # main body
        for char, available in freq.items():
            if available == 0 or char == ")" and is_balanced():
                continue
            freq[char] -= 1
            rec_search(prefix + char)
            # backtrack
            freq[char] += 1

    rec_search("")
    return result


def true_rec(n):
    # base case
    if n == 1:
        result = set(["()"])
        return result
    # main body
    prev = true_rec(n - 1)
    result = set()
    result = result.union(set(["(" + elem + ")" for elem in prev]))
    result = result.union(set(["()" + elem for elem in prev]))
    result = result.union(set([elem + "()" for elem in prev]))
    return result


result = true_rec(6)
print(result)
