dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

num = list(input())

for i in num:
  for j in range(len(dial)):
    if dial[j].find(i) >= 0:
      result += (j + 3)

print(result)