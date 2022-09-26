n, m = map(int, input().split())
badak = [list(input()) for _ in range(n)]
result = n * m
panja = {'-':(0, 1), '|':(1, 0)}
r = 0

def gyesan(x, y, s):
    if x >= n or y >= m:
        return
    if result[x][y] == 0 and badak[x][y] == s:
        result[x][y] = 1
        dx, dy = panja[badak[x][y]]
        gyesan(x + dx, y + dy, badak[x][y])
        return True

# for i in range(n):
#     for j in range(m):
#         if gyesan(i, j, badak[i][j]):
#             r += 1
# print(r)
print(result)