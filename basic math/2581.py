import sys

# 1차
min = int(sys.stdin.readline())
max = int(sys.stdin.readline())
num = []

for i in range(min, max + 1):
  check = 0
  for j in range(1, max + 1):
    if i % j == 0:
      check += 1
    if check > 2:
      break
  if check == 2:
    num.append(i)

if(len(num) == 0):
  print(-1)
else:
  print(sum(num))
  print(num[0])

# 2차
import sys

min = int(sys.stdin.readline())
max = int(sys.stdin.readline())
num = []

for i in range(min, max + 1):
  check = 0
  for j in range(2, i):
    if i % j == 0:
      check += 1
      break
  if check == 0 and i != 1:
    num.append(i)

if(len(num) == 0):
  print(-1)
else:
  print(sum(num))
  print(num[0])

# 3차
import sys

min = int(sys.stdin.readline())
max = int(sys.stdin.readline())
num = []

for i in range(min, max + 1):
  for j in range(2, i + 1):
    if i == j:
      num.append(i)
    if i % j == 0:
      break

if(len(num) == 0):
  print(-1)
else:
  print(sum(num))
  print(num[0])