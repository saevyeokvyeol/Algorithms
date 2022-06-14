import sys

num = list(map(int, sys.stdin.readline().split()))
result = [num[0], num[1], num[2] - num[0], num[3] - num[1]]

print(min(result))