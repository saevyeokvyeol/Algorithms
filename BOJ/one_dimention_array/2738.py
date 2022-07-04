import sys

N, M = list(map(int, sys.stdin.readline().split()))
L = []

for i in range(N * 2):
  L.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
  result = []
  for j in range(M):
    result.append(L[i][j] + L[i + N][j])
  print(*result)