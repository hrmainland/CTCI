# My solution to p04_partition.py
from linked_list import LinkedListNode

def my_partition(ll, x):
    small_dummy, large_dummy = LinkedListNode(0, None), LinkedListNode(0, None)
    small_tail, large_tail = small_dummy, large_dummy
    current = ll.head
    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            small_tail.next = current
        else:
            large_tail.next = current
            
        current = next_node
    small_tail.next = large_dummy.next
    return small_dummy.next