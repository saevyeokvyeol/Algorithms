from math import ceil

n, l, d = map(int, input().split())
for i in range(1, n + 1):
    if ((n + 5) * i - 5) % d < 5:
        print(ceil(((n + 5) * i - 5) / d) * d)
        break