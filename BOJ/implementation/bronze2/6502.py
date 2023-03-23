n = 1
while True:
    try:
        r, w, l = map(int, input().split())
        print("Pizza {} {}".format(n, "fits on the table." if r * 2 >= ((w ** 2) + (l ** 2)) ** 0.5 else "does not fit on the table."))
        n += 1
    except:
        break