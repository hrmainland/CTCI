# My solution to p07_intersection.py
def my_intersection(list1, list2):
    visited = set()
    one = list1.head
    two = list2.head
    while one:
        visited.add(one)
        one = one.next
    while two:
        if two in visited:
            return True
        two = two.next
    return False