n = int(input())
k = 0
answer = 0
while n != 0:
    k += 1
    answer += 1
    if n - k >= 0:
        n -= k
    else:
        k = 1
        n -= k
print(answer)