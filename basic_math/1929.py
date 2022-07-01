import sys

# 1차 풀이
num = list(map(int, sys.stdin.readline().split()))

for i in range(num[0], num[1] + 1):
  check = 0

  for j in range(2, int(i**0.5)+1):
    if i % j == 0:
      check += 1
      break

  if check == 0 and i != 1:
    print(i)

# 에라토스테네스의 체로 응용
num = list(map(int, sys.stdin.readline().split()))

sosu = [True] * (num[1] + 1)

sosu[1] = False

for i in range(2, int(num[1] ** 0.5) + 1):
  if sosu[i] == True:
    for j in range(i * 2, num[1] + 1, i):
      sosu[j] = False

for i in range(num[0], num[1] + 1):
  if sosu[i] == True:
    print(i)