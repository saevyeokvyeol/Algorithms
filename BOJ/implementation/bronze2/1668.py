n = int(input())
trophy = [int(input()) for _ in range(n)]
left = right = 0
lb = rb = 0
for i in range(n):
    if trophy[i] > lb:
        lb = trophy[i]
        left += 1
    if trophy[n - 1 - i] > rb:
        rb = trophy[n - 1 - i]
        right += 1
print(left)
print(right)