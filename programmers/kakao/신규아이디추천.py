def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    
    # 3

    # 4
    if new_id[0] == ".":
        new_id = new_id[1:]
    if new_id[-1] == ".":
        new_id = new_id[:-1]

    # 5
    if len(new_id) == 0:
        new_id = 'a'
    
    # 6
    if len(new_id) >= 16:
        if new_id[15] == ".":
            new_id = new_id[:15]
        else:
            new_id = new_id[:16]
    
    # 7
    if len(new_id) <= 2:
        new_id += (new_id[-1] * (3 - len(new_id)))

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm."))