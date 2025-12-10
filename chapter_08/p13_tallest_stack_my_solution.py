# My solution to p13_tallest_stack.py
import unittest
from functools import reduce


def dfs(box, box_dict, max_heights):
    if max_heights.get(box):
        return max_heights[box]
    extra_height = 0
    for c_box in box_dict[box]:
        extra_height = max(extra_height, dfs(c_box, box_dict, max_heights))
    result = box.height + extra_height
    max_heights[box] = result
    return result


def tallest_stack(boxes):
    boxes.sort(reverse=True)
    box_dict = {}
    for i in range(len(boxes) - 1, -1, -1):
        box = boxes[i]
        box_dict[box] = []
        seen = set()
        for j in range(i + 1, len(boxes)):
            c_box = boxes[j]
            if (
                box.height > c_box.height
                and box.width > c_box.width
                and box.depth > c_box.depth
            ):
                seen = seen.union(set(box_dict[c_box]))
                if c_box in seen:
                    continue
                box_dict[box].append(c_box)

    max_heights = {}
    result = 0
    for box in boxes:
        result = max(result, dfs(box, box_dict, max_heights))
    return result


class Box:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def __str__(self):
        return f"{self.height}, {self.width}, {self.depth}"

    def __hash__(self):
        return self.height

    def __lt__(self, other):
        return self.height < other.height

    def __eq__(self, other):
        return self.height == other.height


def test_null():
    assert tallest_stack([]) == 0


def test_single_box():
    assert tallest_stack([Box(3, 2, 1)]) == 3


def test_two_conflicting_boxes():
    assert tallest_stack([Box(3, 2, 1), Box(5, 4, 1)]) == 5


def test_two_stackable_boxes():
    assert tallest_stack([Box(3, 2, 1), Box(6, 5, 4)]) == 9


class TestTallestStack(unittest.TestCase):
    def test_null(self):
        self.assertEqual(tallest_stack([]), 0)

    def test_single_box(self):
        self.assertEqual(tallest_stack([Box(3, 2, 1)]), 3)

    def test_two_conflicting_boxes(self):
        self.assertEqual(tallest_stack([Box(3, 2, 1), Box(5, 4, 1)]), 5)

    def test_two_stackable_boxes(self):
        self.assertEqual(tallest_stack([Box(3, 2, 1), Box(6, 5, 4)]), 9)


if __name__ == "__main__":
    boxes = [Box(3, 2, 2), Box(6, 5, 4), Box(1, 1, 1), Box(5, 4, 3), Box(2, 2, 2)]
    result = tallest_stack(boxes)
    print(result)
    unittest.main()
