# My solution to p04_check_balanced.py
from tree import *


def depth_dfs(root, depth):
    if not root:
        return None
    if not (root.left or root.right):
        return {"min": depth, "max": depth}
    left_depth = depth_dfs(root.left, depth + 1)
    right_depth = depth_dfs(root.right, depth + 1)
    if not left_depth:
        return right_depth
    if not right_depth:
        return left_depth
    min_depth = min(left_depth["min"], right_depth["min"])
    max_depth = max(left_depth["max"], right_depth["max"])
    return {"min": min_depth, "max": max_depth}


def driver(root):
    depths = depth_dfs(root, 0)
    return depths["max"] - depths["min"] <= 1


# root = create_unbalanced_tree(10)
root = create_tree(10)
print_bfs(root)
depths = driver(root)
print(depths)
