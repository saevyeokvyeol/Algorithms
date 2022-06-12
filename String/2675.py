import sys

T = int(sys.stdin.readline())

for i in range(T):
  string = sys.stdin.readline().split()
  
  result = ""
  for s in string[1]:
    result += s * int(string[0])
  print(result)