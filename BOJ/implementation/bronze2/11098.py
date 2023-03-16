for _ in range(int(input())):
    price = 0
    highest = ""
    for _ in range(int(input())):
        p, name = input().split()
        if price < int(p):
            price = int(p)
            highest = name
    print(highest)