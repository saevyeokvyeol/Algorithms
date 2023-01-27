string = input()
word = "CAMBRIDGE"
for w in word:
    if w in string:
        string = string.replace(w, "")
print(string)