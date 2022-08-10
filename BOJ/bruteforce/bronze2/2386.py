while True:
    s = input()
    if s == "#":
        break
    else:
        a, s = s[0], s[2:].lower()

    print(a, s.count(a))