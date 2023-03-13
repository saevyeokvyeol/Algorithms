word = list(input())
for i in range(len(word)):
    word[i] = chr(ord(word[i]) - 3) if ord(word[i]) > ord("C") else chr(ord(word[i]) + 23)
print("".join(word))