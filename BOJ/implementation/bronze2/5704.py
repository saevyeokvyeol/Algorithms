while True:
    string = input().lower()
    if string == "*": break
    result = "Y"

    for a in range(ord("a"), ord("z") + 1):
        if string.count(chr(a)) == 0:
            result = "N"
    
    print(result)