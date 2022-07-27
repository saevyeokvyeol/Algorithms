import sys

# 풀이 1
N, L, K = list(map(int, sys.stdin.readline().split()))
Q = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
A = S = 0

for i in range(N):
    if Q[i][1] <= L:
        S += 1
    elif Q[i][0] <= L:
        A += 1

if S >= K:
    print(K * 140)
elif S + A < K:
    print(S * 140 + A * 100)
else:
    print(S * 140 + (K - S) * 100)

# 풀이 2
N, L, K = list(map(int, sys.stdin.readline().split()))
A = S = 0

for _ in range(N):
    Q = list(map(int, sys.stdin.readline().split()))
    if Q[1] <= L:
        S += 1
    elif Q[0] <= L:
        A += 1

score = min(S, K) * 140
if S < K:
    score += min(A, K - S) * 100
print(score)