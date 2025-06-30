# My solution to p03_stack_of_plates.py
class StackOfStacks:
    def __init__(self, threshold):
        self.stacks = []
        self.threshold = threshold

    def __str__(self):
        result = ""
        for i in range(1, len(self.stacks) + 1):
            result += f"Stack {i}:\n"
            result += str(self.stacks[i - 1]) + "\n\n"
        return result

    def pop(self):
        if not self.stacks:
            raise Exception("Nothing to pop")
        stack = self.stacks[-1]
        element = stack.pop()
        if not stack:
            self.stacks.pop()
        return element

    def push(self, val):
        if not self.stacks or len(self.stacks[-1]) >= self.threshold:
            self.stacks.append([val])
        else:
            self.stacks[-1].append(val)

    def pop_at(self, index):
        upper_index = index // self.threshold
        lower_index = index % self.threshold
        stack = self.stacks[upper_index]
        elem = stack.pop(lower_index)
        if not stack:
            self.stacks.pop(upper_index)
        return elem


tester = StackOfStacks(1)

for i in range(10):
    tester.push(i)

# for _ in range(5):
#     tester.pop()


print(tester)

print(tester.pop_at(4))

print(tester)
