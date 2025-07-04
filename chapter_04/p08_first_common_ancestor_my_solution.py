# My solution to p08_first_common_ancestor.py
from binary_tree import BinaryTree

t = BinaryTree()
n1 = t.insert(1, None)
n2 = t.insert(2, n1)
n3 = t.insert(3, n1)
n4 = t.insert(4, n2)
n5 = t.insert(5, n2)
n7 = t.insert(7, n3)
n8 = t.insert(8, n4)

t.print_ascii_tree()


def lca(node, target_1, target_2):
    if not node:
        return None
    if node == target_1 or node == target_2:
        return node
    left = lca(node.left, target_1, target_2)
    right = lca(node.right, target_1, target_2)
    if left and right:
        return node
    if left:
        return left
    if right:
        return right
    return None


def get_depth(node):
    depth = 0
    while node.parent:
        node = node.parent
        depth += 1
    return depth


def target_lca(target_1, target_2):
    # shallow = [target_1, get_depth(target_1)]
    # deep = [target_2, get_depth(target_2)]
    shallow = {"node": target_1, "depth": get_depth(target_1)}
    deep = {"node": target_2, "depth": get_depth(target_2)}
    if shallow["depth"] > deep["depth"]:
        tmp = shallow
        shallow = deep
        deep = tmp
    while deep["depth"] > shallow["depth"]:
        deep["node"] = deep["node"].parent
        deep["depth"] -= 1
    while deep["node"] != shallow["node"]:
        deep["node"] = deep["node"].parent
        shallow["node"] = shallow["node"].parent
    return deep["node"]


# result = lca(n1, n8, n4)
# print(result)
result = target_lca(n5, n8)
print(result)
