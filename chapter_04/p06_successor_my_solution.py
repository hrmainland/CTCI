# My solution to p06_successor.py
from tree import *

root = create_bst(10)
print_tree(root)

# go to root
# at each level if value is larger or equal go left, smaller go right
# return current closest when backtracking
