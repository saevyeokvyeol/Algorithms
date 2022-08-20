a, b, n, w = map(int, input().split())
result = [[i, n - i] for i in range(1, n) if a * i + b * (n - i) == w]
if len(result) == 1:
    print(*result[0])
else:
    print(-1)