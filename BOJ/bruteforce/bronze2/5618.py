# 풀이 1
n = int(input())
num = list(map(int, input().split()))
result = []
for i in range(1, min(num) + 1):
    Y = 0
    for j in num:
        if j % i == 0:
            Y += 1
        else:
            break
    if Y == n:
        result.append(i)
print(*result, sep="\n")

# 풀이 2
from math import gcd

n = int(input())
num = gcd(*list(map(int, input().split())))
for i in range(1, num + 1):
    if num % i == 0:
        print(i)