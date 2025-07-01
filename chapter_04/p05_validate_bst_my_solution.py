# My solution to p05_validate_bst.py
from tree import *

root = create_tree(10)
print_bfs(root)


def validate_bst(root):
    if not root:
        return True
    if not (root.left or root.right):
        return True
    if root.left and root.left.val > root.val:
        return False
    if root.right and root.right.val < root.val:
        return False
    return validate_bst(root.left) and validate_bst(root.right)


print(validate_bst(root))
