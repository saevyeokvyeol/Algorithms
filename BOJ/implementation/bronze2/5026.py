for _ in range(int(input())):
    question = input()
    if '+' in question:
        n, m = map(int, question.split('+'))
        print(n + m)
    else:
        print("skipped")