for _ in range(int(input())):
    name = input()
    b = name.lower().count("b")
    g = name.lower().count("g")
    
    keyword = "NEUTRAL"
    if b > g:
        keyword = "A BADDY"
    elif g > b:
        keyword = "GOOD"

    print("{} is {}".format(name, keyword))