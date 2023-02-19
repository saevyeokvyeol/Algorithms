for _ in range(int(input())):
    n = int(input())
    store = list(map(int, input().split()))
    print((max(store) - min(store)) * 2)