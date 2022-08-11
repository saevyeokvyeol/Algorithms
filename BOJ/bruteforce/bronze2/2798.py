N, M = map(int, input().split())
C = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if result < C[i] + C[j] + C[k] <= M:
                result = C[i] + C[j] + C[k]

print(result)