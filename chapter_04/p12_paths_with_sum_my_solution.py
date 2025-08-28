# My solution to p12_paths_with_sum.py
from tree import *

count = 0


def find_paths(root, target):
    global count
    if not root:
        return []
    left_paths = find_paths(root.left, target)
    right_paths = find_paths(root.right, target)
    left_paths.extend(right_paths)
    for i in range(len(left_paths)):
        left_paths[i] = left_paths[i] + root.val
    left_paths.append(root.val)
    for elem in left_paths:
        if elem == target:
            count += 1
            print(root)
    return left_paths


root = create_tree(50)
print_tree(root)

find_paths(root, 94)
print(count)
