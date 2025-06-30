# My solution to p02_check_permutation.py
from collections import Counter
import unittest


def is_permutation(str_a: str, str_b: str):
    freq_a = Counter(str_a)
    freq_b = Counter(str_b)
    return freq_a == freq_b


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [is_permutation]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                self.assertEqual(check_permutation(str1, str2), expected)


if __name__ == "__main__":
    unittest.main()
