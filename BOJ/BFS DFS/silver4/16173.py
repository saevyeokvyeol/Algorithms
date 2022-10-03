# DFS
# 풀이 1
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]

def escape(x, y):
    if x >= n or y >= n:
        return
    d = map[x][y]
    if d == -1:
        print("HaruHaru")
        exit()
    else:
        escape(x + d, y) 
        escape(x, y + d)
escape(0, 0)
print("Hing")

# 풀이 2
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]

def escape(x, y):
    if x >= n or y >= n:
        return
    if result[x][y] == 0:
        result[x][y] = 1
        d = map[x][y]
        escape(x + d, y) 
        escape(x, y + d)

escape(0, 0)
print("HaruHaru" if result[-1][-1] == 1 else "Hing")

# BFS
from collections import deque
n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]
dx = [1, 0]
dy = [0, 1]

def jelly(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + map[x][y] * dx[i]
            ny = y + map[x][y] * dy[i]
            if nx >= n or ny >= n:
                continue
            if result[nx][ny] == 0:
                result[nx][ny] = 1
                queue.append((nx, ny))

jelly(0, 0)
print("HaruHaru" if result[-1][-1] else "Hing")