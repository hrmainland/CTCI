class Node:
    def __init__(self, next, val):
        self.next = next
        self.val = val


def remove_node(head, target):

    if not head:
        return None

    if head.val == target:
        return head.next

    while curr.next:
        # standard case
        if curr.next.val == target:
            curr.next = curr.next.next
            return head

        curr = curr.next
    return head


def reverse(head):
    prev = None
    while head.next:
        next = head.next
        head.next = prev
        prev = head
        head = next
    head.next = prev
    return head


d = Node(None, 9)
c = Node(d, 8)
b = Node(c, 7)
a = Node(b, 6)

# head = remove_node(a, 6)

head = reverse(a)

node = head
while node:
    print(node.val)
    node = node.next
