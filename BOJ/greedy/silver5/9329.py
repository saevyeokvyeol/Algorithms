import sys

# 풀이 1(문제 잘못 본 풀이)
for _ in range(int(sys.stdin.readline())):
    n = list(map(int, sys.stdin.readline().split()))
    k = [list(map(int, sys.stdin.readline().split())) for _ in range(n[0])]
    C = list(map(int, sys.stdin.readline().split()))
    price = 0
    
    m = 100
    for i in range(n[0]):
        for j in range(1, k[i][0] + 1):
            m = min(m, C.count(k[i][j]))
        price += m * k[i][-1]

    print(price)

# 풀이 2
for _ in range(int(sys.stdin.readline())):
    n = list(map(int, sys.stdin.readline().split()))
    k = [list(map(int, sys.stdin.readline().split())) for _ in range(n[0])]
    C = list(map(int, sys.stdin.readline().split()))
    price = 0
    
    for i in range(n[0]):
        m = 100
        for j in range(1, k[i][0] + 1):
            m = min(m, C[k[i][j] - 1])
        price += m * k[i][-1]

    print(price)