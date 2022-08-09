N = int(input())
result = 0
for B in range(1, 501):
    for A in range(B, 501):
        if A ** 2 - N == B ** 2:
            result += 1
print(result)