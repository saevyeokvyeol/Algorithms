while True:
    number = input()
    if number == '0': break

    n, number = number[0], list(number[2:].split())
    submit = [number[0]]

    for num in number:
        if num != submit[-1]:
            submit.append(num)

    print(*submit, "$")