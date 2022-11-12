def solution(numbers, direction):
    if direction == "left":
        n = numbers.pop(0)
        numbers.append(n)
    else:
        n = numbers.pop()
        numbers.insert(0, n)
    return numbers