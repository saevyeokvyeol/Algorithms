from math import ceil
def solution(progresses, speeds):
    bapo = []
    answer = []

    for i in range(len(speeds)):
        bapo.append(ceil((100 - progresses[i]) / speeds[i]))
        
    while len(bapo) > 0:
        result = 1
        if len(bapo) == 1:
            answer.append(result)
            break

        for i in range(1, len(bapo)):
            if(bapo[i] <= bapo[0]):
                result += 1
            else:
                del bapo[:i]
                break

            if(i == len(bapo) - 1):
                bapo.clear()
            
        answer.append(result)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))