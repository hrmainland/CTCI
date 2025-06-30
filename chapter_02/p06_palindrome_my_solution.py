# My solution to p06_palindrome.py
def my_is_palindrome(ll):
    left = right = ll.head
    left_moves = True
    while right:
        right = right.next
        if left_moves:
            left = left.next
        left_moves = not left_moves
    
    mid = right
    right = left
    left = ll.head
    
    stack = []
    while right:
        stack.append(right.value)
    
    while left != mid:
        if left.value != stack.pop():
            return False
    return True
        
        
        
    
    
# racecar  
# 7  

# abba

# ecar
# rac