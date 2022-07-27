import sys

N, A, B = map(int, sys.stdin.readline().split())
G = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
result = "Nae ga wae"

for i in range(8 - N):
    J, V = G[i][0], G[i][1]
    A += J * 3
    B += (J + min(V, 6 - J)) * 3
    if A >= 66 and B >= 130:
        result = "Nice"
        break
print(result)