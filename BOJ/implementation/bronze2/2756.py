target = [[3, 100], [6, 80], [9, 60], [12, 40], [15, 20]]

for _ in range(int(input())):
    input_value = list(map(float, input().split()))
    coodinate = [input_value[i * 2:(i + 1) * 2] for i in range((len(input_value) + 2 - 1) // 2)]
    
    score = [0] * 2
    cnt = 0
    for x, y in coodinate:
        c = (abs(x) ** 2 + abs(y) ** 2) ** 0.5
        for r, s in target:
            if c <= r:
                score[cnt // 3] += s
                break
        cnt += 1

    max_score = max(score)
    print("SCORE: {} to {},".format(score[0], score[1]), end=" ")
    print("TIE." if score.count(max_score) > 1 else "PLAYER {} WINS.".format(score.index(max_score) + 1))