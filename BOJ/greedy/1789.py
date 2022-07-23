# 풀이 1
S = int(input())
result = 0

for i in range(S):
    if S - i > i:
        S -= i
        result += 1
    else:
        break

print(result)

# 풀이 2
S = int(input())
N = 1

while N * (N + 1) / 2 <= S:
    N += 1

print(N - 1)