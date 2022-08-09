# 풀이 1
a, m = map(int, input().split())
i = 1
while True:
    if a * i % m == 1:
        print(i)
        break
    else:
        i += 1

# 풀이 2
a, m = map(int, input().split())
i = 1
while a * i % m != 1:
    i += 1
print(i)