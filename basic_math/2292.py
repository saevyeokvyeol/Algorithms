num = int(input())

result = 1

while num > 1:
  num -= (6 * result)
  result += 1
  
print(result)