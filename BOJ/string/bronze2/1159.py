player = [input() for _ in range(int(input()))]
alpha = []
for i in range(97, 123):
    cnt = 0
    for p in player:
        if p.startswith(chr(i)):
            cnt += 1
        if cnt == 5:
            alpha.append(chr(i))
            break
if len(alpha):
    print(*alpha, sep="")
else:
    print("PREDAJA")