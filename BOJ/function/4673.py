def solve():
  list = set(range(1, 10001))
  num = set()
  for i in range(10001):
    for j in str(i):
      i += int(j)
    num.add(i)
  list = sorted(list - num)
  for i in list:
    print(i)

solve()