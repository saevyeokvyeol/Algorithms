def convert(num, n):
    sum = 0
    while num > 0:
        sum += num % n
        num //= n
    return sum

for i in range(2992, 10000):
    if convert(i, 10) == convert(i, 12) == convert(i, 16):
        print(i)