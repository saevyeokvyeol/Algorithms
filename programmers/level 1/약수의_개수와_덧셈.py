# 첫 번째 풀이
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer += i if get_divisor(i) % 2 == 0 else i * -1
    return answer

def get_divisor(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    return cnt

# 두 번째 풀이
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer += i * -1 if int(i ** 0.5) == i ** 0.5 else i
    return answer