import sys

T = int(sys.stdin.readline())

for i in range(T):
  num = list(map(int, sys.stdin.readline().rstrip().split()))
  print(num[0] + num[1])