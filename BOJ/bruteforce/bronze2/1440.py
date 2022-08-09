time = list(map(int, input().split(":")))
result = 0
for i in time:
    if i >= 60:
        result = 0
        break
    elif 0 < i < 13:
        result += 2
print(result)