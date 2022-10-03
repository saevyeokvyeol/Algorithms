# DFS
c = int(input())
result = [False] * (c + 1)
computer = [[] for _ in range(c + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(computer, 1, result)
print(result.count(True) - 1)

# BFS
from collections import deque

c = int(input())
result = [False] * (c + 1)
computer = [[] for _ in range(c + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(computer, 1, result)
print(result.count(True) - 1)