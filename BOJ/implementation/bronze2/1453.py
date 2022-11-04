n = int(input())
customer = set(map(int, input().split()))
print((len(customer) - n) * -1)