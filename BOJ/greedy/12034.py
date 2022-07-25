import sys

for i in range(int(sys.stdin.readline())):
    C = int(sys.stdin.readline())
    P = list(map(int, sys.stdin.readline().split()))
    R = []
    for j in P:
        if P.count(j + (j // 3)) >= 1:
            R.append(j)
            P.remove(j + (j // 3))
        if len(R) == C:
            break
    print("Case #%d:" % (i + 1), *R)