while True:
    n = int(input())
    if n == 0:
        break
    while n > 9:
        n = sum([int(i) for i in str(n)])
    print(n)