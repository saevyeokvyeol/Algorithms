from math import ceil
import sys

num = list(map(int, sys.stdin.readline().split()))
length = num[0] - num[1]

if(num[2] % length > num[0]):
  result = ceil(num[2] / length)
else:
  result = ceil((num[2] - num[0]) / length) + 1

print(result)