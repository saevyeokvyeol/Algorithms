a, b = input().split()
n, m = len(a), len(b)
cross = set(a).intersection(b)
x = min([a.index(c) for c in cross])
y = b.index(a[x])

for i in range(m):
    for j in range(n):
        if i == y:
            print(a[j], end="")
        elif j == x:
            print(b[i], end="")
        else:
            print(".", end="")
    print()