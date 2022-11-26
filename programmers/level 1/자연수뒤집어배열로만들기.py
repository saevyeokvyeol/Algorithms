def solution(n):
    answer = list(map(int, list(str(n))))
    answer.reverse()
    return answer

print(solution(12345))