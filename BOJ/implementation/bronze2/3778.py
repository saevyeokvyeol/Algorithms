for i in range(int(input())):
    first = input()
    second = input()
    distance = 0
    
    for a in range(ord("a"), ord("z") + 1):
        distance += abs(first.count(chr(a)) - second.count(chr(a)))
        
    print("Case #{}: {}".format(i + 1, distance))