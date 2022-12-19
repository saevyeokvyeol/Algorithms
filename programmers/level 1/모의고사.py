def solution(answers):
    supo = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0] * 3
    for i in range(len(answers)):
        for j in range(len(supo)):
            if answers[i] == supo[j][i % len(supo[j])]:
                score[j] += 1
    return [i + 1 for i in range(3) if score[i] == max(score)]