from collections import deque

# My solution to p01_route_between_nodes.py
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["B", "C"],
    "E": ["C", "F"],
    "F": ["E", "O", "I", "G"],
    "G": ["F", "H"],
    "H": ["G"],
    "I": ["F", "J"],
    "O": ["F"],
    "J": ["K", "L", "I"],
    "K": ["J"],
    "L": ["J"],
    "P": ["Q", "R"],
    "Q": ["P", "R"],
    "R": ["P", "Q"],
}


def dfs(node, target, visited, graph):
    visited.add(node)
    if node == target:
        return True
    for child in graph[node]:
        if child not in visited:
            result = dfs(child, target, visited, graph)
            if result:
                return True
    return False


def is_path(graph, start, target):
    visited = set()
    return dfs(start, target, visited, graph)


def bidirectional(graph, start, target):
    left_q, right_q = deque([start]), deque([target])
    while left_q or right_q:
        if left_q:
            node = left_q.pop()
            if node in right_visited:
                return True
            for child in graph[node]:
                if child not in left_visted:
                    left_visted.add(child)
                    left_q.appendleft(child)
        if right_q:
            node = right_q.pop()
            if node in left_visted:
                return True
            for child in graph[node]:
                if child not in right_visited:
                    right_visited.add(child)
                    right_q.appendleft(child)
    return False


result = bidirectional(graph, "A", "C")
print(result)
