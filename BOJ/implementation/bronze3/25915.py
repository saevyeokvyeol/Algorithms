c = input()
if c > "I":
    print(84 + (ord(c) - ord("I")))
elif c < "I":
    print(84 + (ord("I") - ord(c)))
else:
    print(84)