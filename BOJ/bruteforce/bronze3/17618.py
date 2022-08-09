N = int(input())
result = 0
for i in range(1, N + 1):
    D = sum(list(map(int, list(str(i)))))
    if i % D == 0:
        result += 1
print(result)