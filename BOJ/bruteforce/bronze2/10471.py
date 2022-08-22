W, P = map(int, input().split())
N = list(map(int, input().split()))

R = []
for i in range(P):
    R.append(N[i] - sum(R))
R.append(W - N[-1])

C = R
for i in range(P + 2):
    for j in range(i + 2, P + 2):
        C.append(sum(R[i:j]))

print(*sorted(list(set(C))))