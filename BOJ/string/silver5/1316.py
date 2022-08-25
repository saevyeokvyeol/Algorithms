import sys

T = int(sys.stdin.readline())
result = 0

for i in range(T):
  word = list(sys.stdin.readline().rstrip())
  check = []

  for j in range(len(word) - 1):
    if word[j] != word[j + 1]:
      check.append(word[j])
  check.append(word[-1])

  if len(check) == len(set(check)):
    result += 1

print(T - result)

#############################################################

T = int(sys.stdin.readline())
result = T

for i in range(T):
  word = list(sys.stdin.readline().rstrip())
  for j in range(len(word) - 1):
    if word[j] == word[j + 1]:
      continue
    elif word[j] in word[j + 1:]:
      result -= 1

print(result)