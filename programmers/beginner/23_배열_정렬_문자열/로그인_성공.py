def solution(id_pw, db):
    answer = "fail"
    for d in db:
        if d == id_pw:
            answer = "login"
            break
        elif d[0] == id_pw[0]:
            answer = "wrong pw"
            break
    return answer