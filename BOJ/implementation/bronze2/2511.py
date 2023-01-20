A = map(int, input().split())
B = map(int, input().split())
total_a = total_b = 0
winner = None
for a, b in zip(A, B):
    if a > b:
        total_a += 3
        winner = "A"
    elif b > a:
        total_b += 3
        winner = "B"
    else:
        total_a += 1
        total_b += 1
print(total_a, total_b)
if total_a > total_b:
    print("A")
elif total_b > total_a:
    print("B")
else:
    print(winner if winner != None else "D")