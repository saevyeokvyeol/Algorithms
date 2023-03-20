a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
print(0 if a == b else b - a - 1)
if a != b :
    print(*[i for i in range(a + 1, b)])