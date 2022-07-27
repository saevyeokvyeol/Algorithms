# 풀이 1
N = int(input())
t = sorted(list(map(int, input().split())), reverse=True)
day = 0
for i in range(N):
    if day < t[i] + i + 2:
        day = t[i] + i + 2
print(day)

# 풀이 2
N = int(input())
t = sorted(list(map(int, input().split())), reverse=True)
for i in range(N):
    t[i] += i + 2
print(max(t))