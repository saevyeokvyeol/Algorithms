# 풀이 1
alpha = [chr(i) for i in range(65, 91)]
word = list(input())
result = 0
for i in range(len(word)):
    if i == 0:
        result += min(alpha.index(word[i]), sorted(alpha, reverse=True).index(word[i]) + 1)
    else:
        max_w = max(alpha.index(word[i - 1]), alpha.index(word[i]))
        min_w = min(alpha.index(word[i - 1]), alpha.index(word[i]))
        if max_w - min_w > len(alpha) // 2:
            result += (len(alpha) - max_w) + min_w
        else:
            result += max_w - min_w
print(result)

# 풀이 2
word = input()
result = 0
now = 'A'
for w in word:
    length = abs(ord(now) - ord(w))
    result += min(length, 26 - length)
    now = w
print(result)
