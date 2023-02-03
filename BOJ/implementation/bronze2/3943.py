for _ in range(int(input())):
    n = int(input())
    max = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
            if max < n:
                max = n
    print(max)