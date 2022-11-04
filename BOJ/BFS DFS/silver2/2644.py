# DFS 1
n = int(input())
chon = [[] for _ in range(n + 1)]
result = [0] * (n + 1)
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    chon[x].append(y)
    chon[y].append(x)

def dfs(start, end, chon, result, i):
    if result[start] != 0:
        return
    result[start] = i
    if start == end:
        return
    for c in chon[start]:
        dfs(c, end, chon, result, i + 1)

dfs(a, b, chon, result, 0)
print(result[b] if result[b] else -1)

# DFS 2
n = int(input())
chon = [[] for _ in range(n + 1)]
result = [-1] * (n + 1)
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    chon[x].append(y)
    chon[y].append(x)

def dfs(start, end, chon, result):
    if result[start] == -1:
        result[start] = 0
    if start == end:
        return
    for c in chon[start]:
        if result[c] == -1:
            result[c] = result[start] + 1
            dfs(c, end, chon, result)

dfs(a, b, chon, result)
print(result[b])

# DFS 2
n = int(input())
chon = [[] for _ in range(n + 1)]
result = [0] * (n + 1)
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    chon[x].append(y)
    chon[y].append(x)

def dfs(node):
    for c in chon[node]:
        if result[c] == 0:
            result[c] = result[node] + 1
            dfs(c)

dfs(a)
print(result[b] if result[b] > 0 else -1)

# BFS
from collections import deque

n = int(input())
chon = [[] for _ in range(n + 1)]
result = [-1] * (n + 1)
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    chon[x].append(y)
    chon[y].append(x)
    
def bfs(start, end, chon, result):
    queue = deque([start])
    result[start] = 0
    while queue:
        v = queue.popleft()
        if v == end:
            return
        for c in chon[v]:
            if result[c] == -1:
                result[c] = result[v] + 1
                queue.append(c)
                
bfs(a, b, chon, result)
print(result[b])