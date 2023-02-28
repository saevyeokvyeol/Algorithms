for _ in range(int(input())):
    P, M = map(int, input().split())
    chamga = set()
    for p in range(P):
        chamga.add(int(input()))
    print(P - len(chamga))