n, m = map(int, input().split())
s = list(map(int, input().split()))
s.extend([0] * m)
t = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n + m):
        s[i] -= t[i][j]
        s[j] += t[i][j]
print(*s)