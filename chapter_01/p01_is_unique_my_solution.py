# My solution to p01_is_unique.py

def is_unique(input: str):
    my_set = set()
    for char in input:
        if char in my_set:
            return False
        my_set.add(char)
    return True

    
def no_add(string: str):
    

