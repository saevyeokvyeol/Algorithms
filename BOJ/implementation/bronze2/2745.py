base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b, n = input().split()
n = int(n)
lb = len(b)
print(sum([base.index(bs) * (n ** i) for bs, i in zip(b[::-1], range(lb))]))