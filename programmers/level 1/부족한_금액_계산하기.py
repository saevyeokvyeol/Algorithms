def solution(price, money, count):
    total_price = 0
    for i in range(1, count + 1):
        total_price += price * i
    return 0 if total_price <= money else total_price - money