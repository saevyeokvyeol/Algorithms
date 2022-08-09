N, L = map(int, input().split())
i = 0
while N > 0:
    i += 1
    if not str(L) in str(i):
        N -= 1
print(i)