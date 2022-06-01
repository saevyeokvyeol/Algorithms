import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
  scores = list(sys.stdin.readline().rstrip())
  result = 0
  correct = 0

  for answer in scores:
    if answer == 'O':
      correct += 1
      result += correct
    else:
      correct = 0
  
  print(result)