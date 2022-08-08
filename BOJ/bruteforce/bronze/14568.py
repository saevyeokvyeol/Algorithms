# 풀이 1
N = int(input())
result = 0
for i in range(2, N - 1, 2):
    for j in range(1, N - i + 1):
        for k in range(3, N - i - j + 1):
            if i + j + k == N and j + 2 <= k:
                result += 1
                break
print(result)

# 풀이 2
N = int(input())
result = 0
for i in range(2, N - 1, 2):
    for j in range(1, N - i + 1):
        if N - i - j >= j + 2:
            result += 1
        else:
            break
print(result)

# 풀이 2
N = int(input())
result = 0
i = 0
for i in range(2, N - 1, 2):
    result += (N - i - 2) // 2
print(result)