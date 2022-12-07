def solution(num, total):
    first = int(total / num - num / 2 + 0.5)
    return [first + i for i in range(num)]