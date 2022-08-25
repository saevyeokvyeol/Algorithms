import sys

cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

str = sys.stdin.readline().rstrip()

for c in cro:
  str = str.replace(c, '0')

print(len(str))