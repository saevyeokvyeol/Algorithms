n, c = map(int, input().split())
s = [int(input()) for _ in range(n)]
s.sort()
answer = 0
for i in range(s[0], c + 1):
    for j in s:
        if i % j == 0:
            answer += 1
            break
print(answer)