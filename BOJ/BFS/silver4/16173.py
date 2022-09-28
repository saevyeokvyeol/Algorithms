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