def solution(common):
    difference = common[1] - common[0]
    if common[2] - common[1] != difference:
        difference = common[2] // common[1]
        return common[-1] * difference
    return common[-1] + difference