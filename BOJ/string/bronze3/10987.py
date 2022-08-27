s = input()
M = ['a', 'e', 'i', 'o', 'u']
result = 0
for m in M:
    result += s.count(m)
print(result)