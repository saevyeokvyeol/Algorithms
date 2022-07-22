poly = input()
poly = poly.replace('XXXX', 'AAAA').replace('XX', 'BB')
if poly.count('X') > 0:
    print(-1)
else:
    print(poly)