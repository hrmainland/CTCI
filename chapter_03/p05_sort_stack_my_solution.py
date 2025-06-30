# My solution to p05_sort_stack.py
class MaxStack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def __str__(self):
        return f"main: {str(self.main_stack)}\nmax: {str(self.max_stack)}"

    def push(self, elem):
        self.main_stack.append(elem)
        prev = self.max_stack[-1] if self.max_stack else elem
        self.max_stack.append(max(prev, elem))

    def pop(self):
        if not len(self.main_stack):
            raise Exception("Nothing to pop")
        self.max_stack.pop()
        return self.main_stack.pop()


def higher(ms_1: MaxStack, ms_2: MaxStack):
    if not ms_1.main_stack and not ms_2.main_stack:
        raise Exception("Both stacks empty, can't compare")
    elif not ms_1.main_stack:
        return ms_2
    elif not ms_2.main_stack:
        return ms_1
    if ms_1.max_stack[-1] > ms_2.max_stack[-1]:
        return ms_1
    return ms_2


def sort(stack):
    ms1, ms2 = MaxStack(), MaxStack()

    one = True
    while stack:
        if one:
            ms1.push(stack.pop())
        else:
            ms2.push(stack.pop())
        one = not one

    while ms1.main_stack or ms2.main_stack:
        target_stack = higher(ms1, ms2)
        other_stack = ms1 if target_stack == ms2 else ms2
        max_val = target_stack.max_stack[-1]
        elem = target_stack.pop()
        while elem != max_val:
            other_stack.push(elem)
            elem = target_stack.pop()
        stack.append(elem)


stack = [3, 4, 1, 1, 7, 6, 5, 4, 9]
sort(stack)
print(stack)
