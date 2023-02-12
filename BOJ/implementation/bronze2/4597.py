while True:
    string = input()
    if string == '#': break

    even = True if string.count('1') % 2 == 0 else False
    if string[-1] == 'e' and not even or string[-1] == 'o' and even:
        print(string[:-1] + "1")
    else:
        print(string[:-1] + "0")