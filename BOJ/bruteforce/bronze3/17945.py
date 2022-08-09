A, B = map(int, input().split())

result = []
for i in range(-1000, 1001):
    if i * (i + 2 * A) == - B:
        result.append(i)
    if len(result) == 2:
        break
print(*result)