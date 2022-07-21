num = int(input())
seat = list(input())

if seat.count('L') == 0:
    print(num)
else:
    print(num - (seat.count('L') // 2 - 1))