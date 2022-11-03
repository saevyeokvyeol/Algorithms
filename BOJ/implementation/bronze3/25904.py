# 첫 번째 풀이
# n, x = map(int, input().split())
# p = list(map(int, input().split()))
# num = 0
# while True:
#     if p[num % n] < x:
#         print(num % n + 1)
#         break
#     else:
#         num += 1
#         x += 1
      
# 두 번째 풀이  
n, x = map(int, input().split())
p = list(map(int, input().split()))
for i in range(201):
    if p[i % n] < x + i:
        print(i % n + 1)
        break