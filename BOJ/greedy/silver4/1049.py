from math import ceil
import sys

N, M = map(int, sys.stdin.readline().split())
S = [1000] * 2

for _ in range(M):
    ss, es = map(int, sys.stdin.readline().split())
    S[0] = min(S[0], ss)
    S[1] = min(S[1], es)

if N % 6 * S[1] > S[0]:
    print(ceil(N / 6) * S[0])
elif S[1] * 6 > S[0]:
    print(N // 6 * S[0] + N % 6 * S[1])
else:
    print(N * S[1])