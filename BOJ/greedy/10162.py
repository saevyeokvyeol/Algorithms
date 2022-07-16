def buttonCount(T):
    if T % 10 != 0:
        return [-1]
    
    button = [300, 60, 10]
    cnt = []

    for i in button:
        cnt.append(T // i)
        T = T % i
    
    return cnt

T = int(input())
print(*buttonCount(T))