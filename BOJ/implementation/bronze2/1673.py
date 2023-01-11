while True:
    try:
        n, k = map(int, input().split())
        chicken = n
        while n >= k:
            c = n // k
            n = n % k + c
            chicken += c
        print(chicken)
    except:
        break