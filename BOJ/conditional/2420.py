import math
import sys

num = list(map(int, sys.stdin.readline().split()))
result = int(math.fabs(num[0] - num[1]))
print(result)