def solution(num):
    answer = -1
    for i in range(500):
        if num == 1:
            answer = i
            break
        elif num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
    return answer

print(solution(6))
print(solution(16))
print(solution(626331))