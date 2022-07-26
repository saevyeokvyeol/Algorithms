import sys

N = int(sys.stdin.readline())
Min = 100000
Max = 0
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    Min = min(Min, e)
    Max = max(Max, s)
print(max(Max - Min, 0))