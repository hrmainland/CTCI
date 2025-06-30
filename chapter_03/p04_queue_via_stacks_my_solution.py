# My solution to p04_queue_via_stacks.py
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __str__(self):
        return f"s1: {str(self.s1)}\ns2: {str(self.s2)}"

    def move_all(self, start, end):
        while len(start):
            end.append(start.pop())

    def push(self, element):
        self.move_all(self.s2, self.s1)
        self.s1.append(element)

    def pop(self):
        self.move_all(self.s1, self.s2)
        return self.s2.pop()


tester = Queue()
for i in range(10):
    tester.push(i)
    if i % 2 == 0:
        print(tester.pop())


print(tester)
