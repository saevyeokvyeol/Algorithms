N, S, R = map(int, input().split())
M = set(map(int, input().split()))
P = set(map(int, input().split()))
result = []

if len(M & P) > 0:
    M, P = sorted(list(M - P)), sorted(list(P - M))
else:
    M, P = list(M), list(P)

for i in M:
    if P.count(i - 1):
        P.remove(i - 1)
    elif P.count(i + 1):
        P.remove(i + 1)
    else:
        result.append(i)

print(len(result))