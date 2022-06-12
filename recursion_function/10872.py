import sys

num = int(sys.stdin.readline())

def factorial(num):
  if num == 1:
    return 1
  result = 1
  for i in range(2, num):
    result *= factorial(num - 1)
    print(result)
  return result

print(factorial(num))