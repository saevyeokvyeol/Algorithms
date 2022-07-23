N, M = map(int, input().split())
if N > 0:
    book = list(map(int, input().split()))
    result = 1
    box = M

    for b in book:
        if box - b < 0:
            box = M
            result += 1
        box -= b

    print(result if N > 0 else 0)
else:
    print(0)