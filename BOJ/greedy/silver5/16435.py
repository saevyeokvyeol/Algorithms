N, L = map(int, input().split())
fruit = sorted(list(map(int, input().split())))

for i in fruit:
    if i <= L:
        L += 1
    else:
        break

print(L)