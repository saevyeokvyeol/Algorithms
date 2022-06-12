n = 1000
a = [True]*(n + 1)

for i in range(2, int((n * 2) ** 0.5) + 1):
  if a[i] == True:
    for j in range(i + i, n + 1, i):
      a[j] = False

for i in range(2, n + 1):
  if a[i] == True:
    print(i)