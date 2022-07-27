import sys

# 풀이 1
num = int(sys.stdin.readline())
C = [int(sys.stdin.readline()) for _ in range(num)]
result = 0

while C[0] != max(C) or C.count(max(C)) != 1:
    max_C = C.index(max(C[1:]), 1)
    C[max_C] -= 1
    C[0] += 1
    result += 1

print(result)

# 풀이 2
N = int(sys.stdin.readline())
D = int(sys.stdin.readline())
C = sorted([int(sys.stdin.readline()) for _ in range(N - 1)])
result = 0

while C and D <= C[-1]:
    D += 1
    C[-1] -= 1
    result += 1
    C.sort()

print(result)