# My solution to p03_list_of_depths.py
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
        if not self:
            return "None"
        return f"Node: {self.val}"


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

        if count <= n:
            right_node = Node(randint(0, 100), None, None)
            node.right = right_node
            q.append(right_node)
            count += 1

    return root


def get_linked_lists(root):
    lls = []
    q = deque([root])
    while q:
        head = tail = None
        for _ in range(len(q)):
            node = q.popleft()
            if not head:
                head = tail = LLNode(node, None)
            else:
                tail.next = LLNode(node, None)
                tail = tail.next
            if node.left:
                q.append(node.left) 
            if node.right:
                q.append(node.right)
        lls.append(head)
    return lls


root = create_tree(10)
print_bfs(root)
lls = get_linked_lists(root)
for head in lls:
    print(head)
