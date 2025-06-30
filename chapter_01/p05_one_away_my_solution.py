# My solution to p05_one_away.py
import unittest
import time

test_cases = [
    # no changes
    ("pale", "pale", True),
    ("", "", True),
    # one insert
    ("pale", "ple", True),
    ("ple", "pale", True),
    ("pales", "pale", True),
    ("ples", "pales", True),
    ("pale", "pkle", True),
    ("paleabc", "pleabc", True),
    ("", "d", True),
    ("d", "de", True),
    # one replace
    ("pale", "bale", True),
    ("a", "b", True),
    ("pale", "ble", False),
    # multiple replace
    ("pale", "bake", False),
    # insert and replace
    ("pale", "pse", False),
    ("pale", "pas", False),
    ("pas", "pale", False),
    ("pkle", "pable", False),
    ("pal", "palks", False),
    ("palks", "pal", False),
    # permutation with insert shouldn't match
    ("ale", "elas", False),
]


def one_edit_insert(s1, s2):
    tmp = s2
    s2 = max(s2, s1, key=len)
    s1 = min(tmp, s1, key=len)
    
    diff = len(s2) - len(s1)
    if diff > 1:
        return False
    one = two = 0
    found = False
    while one < len(s1) and two < len(s2):
        c1 = s1[one]
        c2 = s2[two]
        if c1 != c2:
            if found:
                return False
            found = True
            if diff > 0:
                two += 1
            elif diff < 0:
                one += 1
            else:
                one += 1
                two += 1
        else:
            one += 1
            two += 1
    return True


for test_case in test_cases:
    result = one_edit_insert(test_case[0], test_case[1])
    if result != test_case[2]:
        print(result, test_case)


# # length is less
# if missing one letter -> True

# # length is more
# if one letter too long -> True

# # lengths are equal
# if one letter replaced -> True

# abcd
# abdcd


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    testable_functions = [one_edit_insert]

    def test_one_away(self):

        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
