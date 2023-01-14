n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
total = []
for d in dice:
    d.sort()
    if sum(d) / 4 == d[0]:
        total.append(50000 + d[0] * 5000)
    elif d[0] == d[1] == d[2] or d[1] == d[2] == d[3]:
        total.append(10000 + d[1] * 1000)
    elif d[0] == d[1] and d[2] == d[3]:
        total.append(2000 + d[0] * 500 + d[2] * 500)
    elif d.count(d[1]) == 2:
        total.append(1000 + d[1] * 100)
    elif d.count(d[2]) == 2:
        total.append(1000 + d[2] * 100)
    else:
        total.append(max(d) * 100)
print(max(total))