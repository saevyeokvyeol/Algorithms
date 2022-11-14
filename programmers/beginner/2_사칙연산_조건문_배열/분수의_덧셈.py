import math
def solution(denum1, num1, denum2, num2):
    # 분모 구하기
    result_num = (num1 * num2) // math.gcd(num1, num2)
    
    # 분자 구하기
    result_denum = denum1 * (result_num // num1) + denum2 * (result_num // num2)
    
    # 분자와 분모의 최대공약수 구하기
    gongyaksu = math.gcd(result_denum, result_num)
    
    # 최대 공약수로 분자와 분모를 나누어 기약분수 만들기
    result_num //= gongyaksu
    result_denum //= gongyaksu
    return [result_denum, result_num]