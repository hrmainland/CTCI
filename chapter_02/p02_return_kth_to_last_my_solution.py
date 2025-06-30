# My solution to p02_return_kth_to_last.py
def kth_to_last(ll, k):
    left = right = ll.head
    for _ in range(k):
        right = right.next
        if not right:
            return None
    while right:
        left = left.next
        right = right.next
    return left
