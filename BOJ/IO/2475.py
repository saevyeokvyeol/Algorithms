import sys

num = list(map(int, sys.stdin.readline().split()))
result = 0

for i in num:
  result += i**2

print(result % 10)