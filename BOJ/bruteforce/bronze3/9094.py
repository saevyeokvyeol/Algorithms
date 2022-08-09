for i in range(int(input())):
    n, m = map(int, input().split())
    result = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if ((a ** 2 + b ** 2 + m) % (a * b)) == 0:
                result += 1
    print(result)