def solution(s1, s2):
    answer = [1 for i in s1 if s2.count(i)]
    return sum(answer)