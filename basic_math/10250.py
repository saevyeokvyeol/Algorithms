import sys

num = int(sys.stdin.readline())

for i in range(num):
  info = list(map(int, sys.stdin.readline().split()))
  N = 1

  while info[2] <= info[0]:
    info[2] -= info[0]
    N += 1
  
  print(str(info[2]) + str(N).zfill(2))