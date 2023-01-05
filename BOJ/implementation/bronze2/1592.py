n, m, l = map(int, input().split())
p = [0] * n
c = 0
count = -1
while p.count(m) == 0:
    p[c] += 1
    c = c + l if p[c] % 2 == 0 else c - l
    c = c % n
    count += 1
print(count)