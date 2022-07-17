# 풀이 1
nums = list(input().split()) 
min = 0
max = 0

for i in nums:
    N = list(i)
    while True:
        try:
            index = N.index('6')
            N[index] = '5'
        except:
            break
    num = ''
    for j in N:
        num += j
    
    num = int(num)
    min += num

    while True:
        try:
            index = N.index('5')
            N[index] = '6'
        except:
            break
    num = ''
    for j in N:
        num += j
    
    num = int(num)
    max += num

print(min, max)

# 풀이 2
nums = list(input().split())
min = 0
max = 0

for i in nums:
    N = list(i)
    min_num = ''
    max_num = ''
    for j in N:
        if j == '5' or j == '6':
            min_num += '5'
            max_num += '6'
        else:
            min_num += j
            max_num += j
    
    min += int(min_num)
    max += int(max_num)

print(min, max)

# 풀이 3
nums = list(input().split())
min = 0
max = 0

for i in nums:
    min += int(i.replace('6', '5'))
    max += int(i.replace('5', '6'))

print(min, max)