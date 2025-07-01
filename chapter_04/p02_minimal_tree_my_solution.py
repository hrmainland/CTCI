# My solution to p02_minimal_tree.py
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node val {self.value}"


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def search_tree(array, start, end):
    if start > end:
        return None
    if start == end:
        this_node = Node(array[start], None, None)
        return this_node
    mid = (start + end) // 2

    left_tree = search_tree(array, start, mid - 1)
    right_tree = search_tree(array, mid + 1, end)
    this_node = Node(array[mid], left_tree, right_tree)
    return this_node


def driver(array):
    return search_tree(array, 0, len(array) - 1)


result = driver(array)

print(result, result.left, result.right)
