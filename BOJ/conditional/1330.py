import sys # sys.stdin.readline() 사용 시 반드시 임포트!

# 방법 1
# num = input().split()
# print(num)

# for i in range(len(num)):
#   num[i] = int(num[i])
# print(num)

# 방법 2
# num = sys.stdin.readline().split()
# print(num)

# for i in range(len(num)):
#   num[i] = int(num[i])
# print(num)

# 방법 3
num = list(   map(   int, sys.stdin.readline().split()   )   )
print(num)

if num[0] > num[1]:
  print(">")
elif num[0] < num[1]:
  print("<")
else:
  print("==")