string = input()
char = input().split()
for c in char:
    string = string.replace(c, c.lower())
print(string)