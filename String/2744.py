string = list(input())

for i in range(len(string)):
  if string[i].isupper():
    string[i] = string[i].lower()
  else:
    string[i] = string[i].upper()

print(*string, sep="")