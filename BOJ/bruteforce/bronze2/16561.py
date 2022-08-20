# 풀이 1
n = int(input())
R = 0
for i in range(3, n + 1, 3):
    for j in range(3, n + 1 - i, 3):
        for k in range(3, n + 1 - i - j, 3):
            if i + j + k == n:
                R += 1
print(R)

# 풀이 2
n = int(input()) // 3
print((n - 1) * (n - 2) // 2)