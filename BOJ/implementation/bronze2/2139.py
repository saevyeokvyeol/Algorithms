import datetime

while True:
    d, m, y = map(int, input().split())
    if d + m + y == 0:
        break

    start = datetime.date(y, 1, 1)
    end = datetime.date(y, m, d)
    print((end - start).days + 1)