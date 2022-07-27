import sys

for _ in range(int(sys.stdin.readline())):
    J, N = map(int, sys.stdin.readline().split())
    box = []
    for _ in range(N):
        R, C = map(int, sys.stdin.readline().split())
        box.append(R * C)
    box.sort()
    result = 0
    while J > 0:
        J -= box.pop()
        result += 1
    print(result)