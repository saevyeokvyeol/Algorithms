# DFS
from sys import setrecursionlimit

setrecursionlimit(10 ** 4)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(bat, x, y, n, m):
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    if bat[x][y] == 1:
        bat[x][y] = 0
        for i in range(4):
            dfs(bat, x + dx[i], y + dy[i], n, m)
        return True
    else:
        return False

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    bat = [[0] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        a, b = map(int, input().split())
        bat[b][a] = 1
    for i in range(n):
        for j in range(m):
            if dfs(bat, i, j, n, m):
                result += 1
    print(result)
    
# BFS
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(bat, x, y, n, m):
    if bat[x][y] == 0:
        return False
    else:
        queue = deque()
        queue.append(((x, y)))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= n or nx < 0 or ny >= m or ny < 0:
                    continue
                if bat[nx][ny] == 0:
                    continue
                else:
                    bat[nx][ny] = 0
                    queue.append((nx, ny))
        return True

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    bat = [[0] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        a, b = map(int, input().split())
        bat[b][a] = 1
    for i in range(n):
        for j in range(m):
            if bfs(bat, i, j, n, m):
                result += 1
    print(result)