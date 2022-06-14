import sys
# 고정비용: 1000  가변비용: 70  판매가격: 170
num = list(map(int, sys.stdin.readline().split()))

if num[1] >= num[2]:
  result = -1
else:
  result = num[0] // (num[2] - num[1]) + 1

print(result)