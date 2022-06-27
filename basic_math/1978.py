num = int(input())
sosu = list(map(int, input().split()))

for i in range(num):
  if sosu[i] == 1:
    num -= 1
    continue

  for j in range(2, int(sosu[i] ** 0.5) + 1):
    if sosu[i] % j == 0:
      num -= 1
      break

print(num)