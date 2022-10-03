a, b = map(int, input().split())

for i in range(3):
    if i % 2 == 0:
        b += a
    else:
        a += b
    if a > 4 or b > 4:
        break
print('yt' if a < b else 'yj')