import sys

A, B = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
result = abs(A - B)
for _ in range(N):
    F = abs(int(sys.stdin.readline()) - B) + 1
    if F < result:
        result = F
print(result)