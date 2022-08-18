result = []
N, K = map(int, input().split())
for j in range(1, K + 1):
    result.append(int(str(N * j)[::-1]))
print(max(result))