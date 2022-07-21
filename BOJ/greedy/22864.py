A, B, C, M = map(int, input().split())
P = W = 0
for _ in range(24):
    if P + A <= M:
        P += A
        W += B
    else:
        P = P - C if P - C >= 0 else 0
print(W)