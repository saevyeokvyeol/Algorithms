stick = [int(input()) for _ in range(int(input()))]
stick.reverse()

max = 0
cnt = 0
for s in stick:
    if max < s:
        cnt += 1
        max = s
print(cnt)