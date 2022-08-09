# 풀이 1
s = []
for i in range(int(input()), int(input()) + 1):
    if (i ** 0.5).is_integer():
        s.append(i)

if len(s):
    print(sum(s))
    print(min(s))
else:
    print(-1)

# 풀이 2
s = [i for i in range(int(input()), int(input()) + 1) if (i ** 0.5).is_integer()]
if len(s):
    print(sum(s))
    print(min(s))
else:
    print(-1)