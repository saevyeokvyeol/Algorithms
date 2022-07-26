n = int(input())
a = sorted(list(map(int, input().split())))
price = 0
length = sum(a)
for i in range(n - 1):
    length -= a[i]
    price += a[i] * length
print(price)