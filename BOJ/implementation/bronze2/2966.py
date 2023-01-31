sg = ['A', 'B', 'C']
cy = ['B', 'A', 'B', 'C']
hj = ['C', 'C', 'A', 'A', 'B', 'B']
id = ["Adrian", "Bruno", "Goran"]
score = [0] * 3

n = int(input())
question = input()

for i, q in zip(range(n), question):
    score[0] += 1 if q == sg[i % len(sg)] else 0
    score[1] += 1 if q == cy[i % len(cy)] else 0
    score[2] += 1 if q == hj[i % len(hj)] else 0

print(max(score))
print(*[id[i] for i in range(3) if max(score) == score[i]], sep="\n")