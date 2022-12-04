def solution(score):
    avg = [sum(s) / 2 for s in score]
    avg_sorted = sorted(avg, reverse=True)
    return [avg_sorted.index(a) + 1 for a in avg]