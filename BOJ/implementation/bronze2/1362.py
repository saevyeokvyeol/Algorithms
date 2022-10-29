i = 1
while True:
    o, w = map(int, input().split())
    state = 0
    if o == w == 0:
        break
    while True:
        j, n = input().split()
        if j == '#':
            break
        elif j == 'E':
            n = '-' + n
        w += int(n)
        if w <= 0:
            state = 1
    if w <= 0 or state == 1:
        print(i, "RIP")
    elif o // 2 < w < o * 2:
        print(i, ":-)")
    else:
        print(i, ":-(")
    i += 1