# My solution to p06_animal_shelter.py
from collections import deque

q = deque()

for i in range(10):
    q.append(i)

for i in range(5):
    q.popleft()

q.appendleft
