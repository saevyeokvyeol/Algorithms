def solution(n):
    return int(get_base(n, 3), base=3)

def get_base(n, base):
    result = ""
    while n > 0:
        n, mod = divmod(n, base)
        result += str(mod)
        print(result)
    return result