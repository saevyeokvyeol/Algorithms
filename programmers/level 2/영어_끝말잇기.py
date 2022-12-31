def solution(n, words):
    word = ""
    for i in range(len(words)):
        if i != words.index(words[i])or len(word) > 0 and words[i][0] != word[-1]:
            return [i % n + 1, int(i // n) + 1]
        word = words[i]
    return [0, 0]