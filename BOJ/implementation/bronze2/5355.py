for _ in range(int(input())):
    sic = input().split()
    result = float(sic.pop(0))
    for s in sic:
        if s == "@":
            result *= 3
        if s == '%':
            result += 5
        if s == '#':
            result -= 7
    print("{:.2f}".format(result))