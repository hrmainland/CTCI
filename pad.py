import heapq

vars = [[0, 6, 5], [1, 3, 3], [0, 2, 2]]

heapq.heapify(vars)
print(vars)

heapq.heapreplace(vars, [7, 7, 7])

print(vars)
