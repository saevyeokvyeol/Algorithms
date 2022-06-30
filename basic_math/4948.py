while True:
  n = int(input())

  if(n == 0): break

  sosu = [True]*((n * 2 + 1))
  result = 0

  for i in range(2, int((n * 2) ** 0.5) + 1):
    if sosu[i] == True:
      for j in range(i + i, ((n * 2) + 1), i):
        sosu[j] = False

  for i in range(n + 1, ((n * 2) + 1)):
    if sosu[i] == True:
      result += 1
  print(result)