string = input()
key = input()
password = ""

for i in range(len(string)):
    if string[i] == " ":
        password += string[i]
        continue
    s = chr(ord(string[i]) - (ord(key[i % (len(key))]) - 96))
    if s < "a":
        s = chr((ord(s)) + 26)
    password += s
    
print(password)