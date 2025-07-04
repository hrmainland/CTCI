# My solution to p10_check_subtree.py
from tree import *

root = create_tree(20)
root.val = 94


sub_root = root.left.left
sub_root.val = 22

print_tree(root)
print_tree(sub_root)


def match(n1, n2):
    if n1 != n2:
        return False
    if not n1:
        return True
    return match(n1.left, n2.left) and match(n2.right, n2.right)


def dfs(n1, n2):
    is_match = match(n1, n2)
    if is_match:
        return True
    return dfs(n1.left, n2) or dfs(n1.right, n2)


print(dfs(root, sub_root))
