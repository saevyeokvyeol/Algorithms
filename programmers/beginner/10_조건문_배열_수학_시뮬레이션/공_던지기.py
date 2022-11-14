def solution(numbers, k):
    answer = 1
    length = len(numbers)
    for i in range(k - 1):
        answer = (answer + 2) % length
    return answer