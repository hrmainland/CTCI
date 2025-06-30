# My solution to p05_sum_lists.py
from linked_list import LinkedList, LinkedListNode

def my_sum_lists(ll_a, ll_b):
    remainder = 0
    left = ll_a.head
    right = ll_b.head
    ll = LinkedList()
    head = LinkedListNode(None, None)
    tail = head
    while left or right:
        left_val = left.value if left else 0
        right_val = right.value if right else 0
        this_sum = left_val + right_val + remainder
        this_digit = this_sum % 10
        remainder = this_sum // 10
        tail.next = LinkedListNode(this_digit, None)
        tail = tail.next
        
        if left:
            left = left.next
        if right:
            right = right.next
    
    if remainder:
        tail.next = LinkedListNode(remainder, None)
        tail = tail.next
        
    ll.head = head.next
    ll.tail = tail
    return ll