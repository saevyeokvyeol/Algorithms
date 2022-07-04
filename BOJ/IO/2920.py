import sys

melody = list(map(int, sys.stdin.readline().split()))
m = sorted(melody)
result = "mixed"

for i in range(len(m)):
  if i == 7:
    result = "ascending"
  if melody[i] != m[i]:
    break

for i in range(len(m)):
  if i == 7:
    result = "descending"
  if melody[i] != m[7 - i]:
    break

print(result)