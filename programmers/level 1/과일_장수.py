def solution(k, m, score):
    score.sort(reverse=True)
    return sum([i * m for i in score[m - 1::m]])