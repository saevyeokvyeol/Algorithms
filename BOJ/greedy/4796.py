import sys

C = 0
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if sum([L, P, V]) == 0:
        break
    C += 1
    result = (V // P) * L + min(V % P, L)
    print("Case %s: %s" % (C, result))