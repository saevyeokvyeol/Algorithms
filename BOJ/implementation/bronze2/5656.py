i = 1

while True:
    a, c, b = input().split()
    a, b = int(a), int(b)
    if c == "E": break
    result = False

    if ">" in c and a > b:
        result = True
    elif "<" in c and a < b:
        result = True
    elif "=" in c and "!" not in c and a == b:
        result = True
    elif "!" in c and a != b:
        result = True
    
    print("Case {}: {}".format(i, "true" if result else "false"))
    i += 1