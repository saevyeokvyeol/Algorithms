mirror = {'b':'d', 'd':'b', 'p':'q', 'q':'p', 'i':'i', 'o':'o', 'v':'v', 'w':'w', 'x':'x'}
mirror_alphabet = mirror.keys()

while True:
    word = input()
    if word == "#": break

    mirror_word = ""
    for w in word[::-1]:
        if w in mirror_alphabet:
            mirror_word += mirror[w]
        else:
            mirror_word = "INVALID"
            break
    print(mirror_word)