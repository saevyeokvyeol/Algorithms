# 풀이 1
result = 0
for i in range(1, int(input()) + 1):
    for s in str(i):
        if s in ['3', '6', '9']:
            result += 1
print(result)

# 풀이 2
result = 0
for i in range(1, int(input()) + 1):
    s = str(i)
    result += s.count('3') + s.count('6') + s.count('9')
print(result)

# 풀이 3
s = []
for i in range(1, int(input()) + 1):
    s.extend(list(str(i)))
print(s.count('3') + s.count('6') + s.count('9'))