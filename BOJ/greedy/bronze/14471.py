# 풀이 1
import sys

N, M = map(int, sys.stdin.readline().split())
dojang = []
result = 0
cnt = M - 1

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    if A >= N:
        cnt -= 1
    else:
        dojang.append(N - A)

dojang.sort()

for i in range(cnt):
    result += dojang[i]

print(result)

# 풀이 2
import sys

N, M = map(int, sys.stdin.readline().split())
dojang = [N - list(map(int, sys.stdin.readline().split()))[0] for _ in range(M)]
cnt = M - 1

for i in range(M):
    if dojang[i] > 0:
        cnt -= 1

if cnt <= 0:
    print(0)
else:
    dojang.sort()
    print(sum(dojang[cnt:M - 1]))