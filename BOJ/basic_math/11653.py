import sys

N = 1000
while N > 1:
  for i in range(2, N + 1):
    if N % i == 0:
      print(i)
      N //= i
      break