result = [x for x in range(1, 31)]

while len(result) > 2:
  result.remove(int(input()))

print(result[0])
print(result[1])