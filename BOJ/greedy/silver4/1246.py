import sys

# 풀이 1
N, M = map(int, sys.stdin.readline().split())
customer = [int(sys.stdin.readline()) for _ in range(M)]
customer.sort(reverse=True)
result = []

for i in range(min(N, M)):
    result.append((i + 1) * customer[i])

total = max(result)
print(customer[result.index(total)], total)

# 풀이 2
N, M = map(int, sys.stdin.readline().split())
customer = [int(sys.stdin.readline()) for _ in range(M)]
customer.sort(reverse=True)
P = 0
T = 0

for i in range(M):
    if T < customer[i] * i + 1:
        P = customer[i]
        T = customer[i] * (i + 1)

print(P, T)