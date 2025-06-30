# O(N)
import unittest


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False

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


class Test(unittest.TestCase):

    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.test_cases:
            actual = string_rotation(s1, s2)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
