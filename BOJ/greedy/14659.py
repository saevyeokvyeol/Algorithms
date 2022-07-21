import sys

N = int(sys.stdin.readline())
mountain = list(map(int, sys.stdin.readline().split()))
result = []
high = enemy = 0

for i in mountain:
    if i < high:
        enemy += 1
    else:
        high = i
        result.append(enemy)
        enemy = 0
result.append(enemy)
print(max(result))