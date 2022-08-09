s1, s2, s3 = map(int, input().split())
s = {}

for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            try:
                s[i + j + k] += 1
            except:
                s[i + j + k] = 1

print(sorted(s.keys(), key=lambda x:-s[x])[0])