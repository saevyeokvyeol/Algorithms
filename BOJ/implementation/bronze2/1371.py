import sys

# a부터 z까지 알파벳의 갯수를 저장하는 리스트 생성
alphabet = [[chr(i), 0] for i in range(ord('a'), ord('z') + 1)]

# 문자열을 입력받음
string = list(sys.stdin.read())

# a부터 z까지 알파벳 갯수를 세서 리스트에 저장
for i in range(26):
    alphabet[i][1] = string.count(chr(ord('a') + i))

# 갯수와 알파벳 순서로 리스트 재정렬
alphabet.sort(key=lambda x:(-x[1], x[0]))

# 가장 많은 글자를 출력
for a in alphabet:
    if a[1] == alphabet[0][1]:
        print(a[0], end="")