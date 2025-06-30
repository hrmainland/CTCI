# My solution to p01_remove_dups.py
from chapter_02.linked_list import LinkedList


def remove_duplicates(ll):
    current = ll.head
    if not current:
        return ll
    seen = set(current.value)
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            
        current = current.next
    return ll
    