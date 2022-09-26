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