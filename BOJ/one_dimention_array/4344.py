import sys

case = int(sys.stdin.readline())

for i in range(case):
  score = list(map(int, sys.stdin.readline().split()))

  avg = sum(score[1:]) / score[0]

  count = 0
  for j in score[1:]:
    if j > avg:
      count += 1

  result = count / score[0] * 100
  print("{0:.3f}%".format(result))