# My solution to p06_string_compression.py

import time
import unittest


import itertools

def compress_string(s):
    if len(s) <= 2:
        return s

    pieces = (
        f"{char}{sum(1 for _ in group)}"
        for char, group in itertools.groupby(s)
    )
    
    compressed = "".join(pieces)
    return s if len(compressed) >= len(s) else compressed


def compress_string(string):
    result = []
    count = 1
    if len(string) <= 2:
        return string

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            result.append(string[i])
            result.append(str(count))
            count = 1
        else:
            count += 1

    result.append(string[-1])
    result.append(str(count))

    string_result = "".join(result)
    if len(string_result) >= len(string):
        return string
    return string_result


# print(compress_string("aabcccccaaa"))


class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    testable_functions = [
        compress_string,
    ]

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert f(test_string) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
