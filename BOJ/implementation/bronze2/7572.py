twelve = 'ABCDEFGHIJKL'
ten = '0123456789'
year = int(input()) + 56
print(twelve[year % 12], ten[year % 10], sep="")