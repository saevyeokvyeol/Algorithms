# 첫 번째 풀이
def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if len(answer) != 0:
        answer.sort()
    else:
        answer.append(-1)
    return answer

# 두 번째 풀이
def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]