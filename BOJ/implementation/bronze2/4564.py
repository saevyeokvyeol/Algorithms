while True:
    num = int(input())
    if num == 0: break

    nums = [num]
    
    while num > 9:
        n = 1
        for i in str(num):
            n *= int(i)
        nums.append(n)
        num = n

    print(*nums)