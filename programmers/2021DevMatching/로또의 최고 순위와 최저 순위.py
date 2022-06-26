def solution(lottos, win_nums):
	answer = []

	result = list(set(lottos).intersection(win_nums))
	answer.append(7 - (len(result) + lottos.count(0)) if (len(result) + lottos.count(0)) > 1 else 6)
	answer.append(7 - len(result) if len(result) > 1 else 6)
	
	return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))