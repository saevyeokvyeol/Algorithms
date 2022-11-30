def solution(spell, dic):
    for d in dic:
        if set(list(d)).intersection(spell) == set(spell):
            return 1
    return 2