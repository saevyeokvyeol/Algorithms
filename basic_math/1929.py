import sys

num = list(map(int, sys.stdin.readline().split()))

for i in range(num[0], num[1] + 1):
  check = 0

  for j in range(2, int(i**0.5)+1):
    if i % j == 0:
      check += 1
      break

  if check == 0 and i != 1:
    print(i)