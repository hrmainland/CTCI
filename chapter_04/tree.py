from random import randint, seed
from collections import deque

seed(42)


class LLNode:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{str(self.val)} with length {self.count()}"

    def count(self):
        current = self
        count = 0
        while current:
            count += 1
            current = current.next
        return count


class Node:
    def __init__(self, val, left, right):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self) -> str:
        left = self.left.val if self.left else "None"
        right = self.right.val if self.right else "None"

        if not self:
            return "None"
        return f"Node: {self.val}, (l: {left}, r: {right})"


def print_tree(node, prefix="", is_left=True):
    if node is None:
        return

    if node.right:
        new_prefix = prefix + ("│   " if is_left else "    ")
        print_tree(node.right, new_prefix, False)

    connector = "└── " if is_left else "┌── "
    print(prefix + connector + str(node.val))

    if node.left:
        new_prefix = prefix + ("    " if is_left else "│   ")
        print_tree(node.left, new_prefix, True)




def print_bfs(root):
    q = deque([root])
    indent = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if not node:
                continue
            print("\t" * indent + str(node))
            q.append(node.left)
            q.append(node.right)
        indent += 1


def create_tree(n):
    root = Node(randint(0, 100), None, None)
    q = deque([root])
    count = 1
    while q:
        node = q.popleft()
        if count < n:
            left_node = Node(randint(0, 100), None, None)
            node.left = left_node
            q.append(left_node)
            count += 1

        if count < n:
            right_node = Node(randint(0, 100), None, None)
            node.right = right_node
            q.append(right_node)
            count += 1

    return root


def create_unbalanced_tree(n):
    root = Node(randint(0, 100), None, None)
    q = deque([root])
    count = 1
    while q:
        node = q.popleft()
        if count < n:
            left_node = Node(randint(0, 100), None, None)
            node.left = left_node
            q.append(left_node)
            count += 1

        if count < n:
            right_node = Node(randint(0, 100), None, None)
            node.right = right_node
            q.append(right_node)
            count += 1

    current = root
    while current.left:
        current = current.left
    current.left = Node(randint(0, 100), None, None)

    return root


def bst_dfs(array, left, right):
    if left > right:
        return None
    if left == right:
        return Node(array[left], None, None)
    mid = (left + right) // 2
    node = Node(array[mid], None, None)
    left_tree = bst_dfs(array, left, mid - 1)
    right_tree = bst_dfs(array, mid + 1, right)
    node.left = left_tree
    node.right = right_tree
    return node


def create_bst(n):
    array = sorted([randint(0, 100) for _ in range(n)])
    print(array)
    return bst_dfs(array, 0, len(array) - 1)
