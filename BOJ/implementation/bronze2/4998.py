while True:
    try:
        n, b, m = map(float, input().split())
        year = 0
        while n < m:
            year += 1
            n += n / 100 * b
        print(year)
    except:
        break