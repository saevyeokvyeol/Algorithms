# 첫 번째 풀이
def solution(num_list, n):
    answer = []
    a = []
    for num in num_list:
        a.append(num)
        if len(a) == n:
            answer.append(a)
            a = []
    return answer

# 두 번째 풀이
def solution(num_list, n):
    answer = [num_list[i * n:i * n + n] for i in range(len(num_list) // n)]
    return answer