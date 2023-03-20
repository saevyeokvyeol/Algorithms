n, m = map(int, input().split())
ball = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    ball[a], ball[b] = ball[b], ball[a]

print(*ball[1:])