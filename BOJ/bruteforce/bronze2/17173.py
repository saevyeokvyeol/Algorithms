N, M = map(int, input().split())
K = list(map(int, input().split()))
R = []
for k in K:
    for i in range(k, N + 1, k):
        R.append(i)
print(sum(set(R)))