n, m = map(int, input().split())
boxs = list(map(int, input().split()))
books = list(map(int, input().split()))
for book in books:
    for i in range(n):
        if boxs[i] >= book:
            boxs[i] -= book
            break
print(sum(boxs))