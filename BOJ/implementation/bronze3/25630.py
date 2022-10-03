n = int(input())
stst = input()
result = 0
for i in range(n // 2):
    if stst[i] != stst[n - 1 - i]:
        result += 1
print(result)