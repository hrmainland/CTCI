# My solution to p11_random_node.py
from random import randint
from tree import create_bst

nodes = []
root = create_bst(100)


def add_nodes(root):
    if not root:
        return
    nodes.append(root)
    add_nodes(root.left)
    add_nodes(root.right)


add_nodes(root)

# print(nodes[randint(0, len(nodes) - 1)])
