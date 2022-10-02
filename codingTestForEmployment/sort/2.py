student = [input().split() for _ in range(int(input()))]
student.sort(key=lambda x:x[1])

for s in student:
    print(s[0], end=" ")

# 예시
# N을 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 정수는 정수형으로 변환해서 저장
    array.append((input_data[0], int(input_data[1])))

# 키(Key)를 이요하여, 정수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')