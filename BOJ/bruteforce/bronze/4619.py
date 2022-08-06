while True:
    B, N = map(int, input().split())
    if B + N == 0:
        break
    i = 0
    while i ** N < B:
        i += 1
    print(i if abs(B - (i - 1) ** N) > abs(B - i ** N) else i - 1)