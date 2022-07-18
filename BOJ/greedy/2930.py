import sys

R = int(sys.stdin.readline())
SG = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
rsp = {"S":"R", "R":"P", "P":"S"}
score = result = 0
max_score = [[0] * 3 for _ in range(R)]

for i in range(N):
    F = sys.stdin.readline()
    for j in range(R):
        if SG[j] == F[j]:
            score += 1
        elif rsp.get(F[j]) == SG[j]:
            score += 2

        if F[j] == "R":
            max_score[j][0] += 1
        elif F[j] == "S":
            max_score[j][1] += 1
        else:
            max_score[j][2] += 1

for m in max_score:
    s = m[0] * 2 + m[2]
    if s < m[1] * 2 + m[0]:
        s = m[1] * 2 + m[0]
    if s < m[2] * 2 + m[1]:
        s = m[2] * 2 + m[1]
    result += s

print(score)
print(result)