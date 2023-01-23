n = int(input())
for _ in range(n):
    string = input()
    pwd = input()
    
    message = ""
    
    for s in string:
        if s == " ":
            message += s
        else:
            message += pwd[ord(s) - 65]
    
    print(message)