num = list(map(int, input().split()))
x = min(num)
while True:
    f = 0
    for i in num:
        if x % i == 0:
            f += 1
    if f >= 3:
        print(x)
        break
    else:
        x += 1