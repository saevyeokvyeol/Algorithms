tip = 0
N = int(input())
C = sorted([int(input()) for _ in range(N)], reverse=True)
for i in range(N):
    tip += max(C[i] - i, 0)
print(tip)