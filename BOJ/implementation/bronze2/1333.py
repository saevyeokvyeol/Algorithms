n, l, d = map(int, input().split())
i = 1
while True:
    if  l <= (i * d) % (l + 5) <= l + 5  or n * (l + 5) - 5 < i * d:
        break
    i += 1
print(i * d)