# 첫 번째 풀이
def solution(n, words):
    for i in range(len(words)):
        if i != words.index(words[i]) or len(word) > 0 and words[i][0] != word[-1]:
            return [i % n + 1, int(i // n) + 1]
        word = words[i]
    return [0, 0]

# 두 번째 풀이
def solution(n, words):
    for i in range(1, len(words)):
        if words[i] in words[:i] or words[i][0] != words[i - 1][-1]:
            return [i % n + 1, int(i // n) + 1]
    return [0, 0]