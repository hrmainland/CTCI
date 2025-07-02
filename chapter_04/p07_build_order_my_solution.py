# My solution to p07_build_order.py

# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

from collections import defaultdict


def dfs(node, adj, stack, visited):
    children = adj.get(node)
    if not children:
        stack.append(node)
        visited.add(node)
        return
    for child in children:
        if child not in visited:
            dfs(child, adj, stack, visited)
    stack.append(node)
    visited.add(node)


def topsort(projects, adj, stack, visited):
    for project in projects:
        if project not in visited:
            dfs(project, adj, stack, visited)
    return stack


def order(projects, dependencies):
    adj = defaultdict(list)
    for link in dependencies:
        adj[link[0]].append(link[1])
    order = topsort(projects, adj, [], set())
    return order[::-1]


projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
result = order(projects, dependencies)
print(result)
