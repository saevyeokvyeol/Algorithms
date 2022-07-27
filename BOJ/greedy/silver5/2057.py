def solution(num):
    factorial = [1]
    result = 'NO'

    for i in range(1, num):
        F = factorial[i - 1] * i
        if F > num:
            break
        factorial.append(F)

    for i in range(len(factorial), 0, -1):
        if factorial[:i].count(num):
            result = 'YES'
            break
        if num > factorial[i - 1]:
            num -= factorial[i - 1]
            
    print(result)

for i in range(50):
    solution(i)