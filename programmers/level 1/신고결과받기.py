def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]

    report = list(set(report))

    count = {}
    for i in range(len(report)):
        report[i] = list(report[i].split())
        if report[i][1] in count:
            count[report[i][1]] += [report[i][0]]
        else:
            count[report[i][1]] = [report[i][0]]
    for id in id_list:
        if id in count:
            if len(count[id]) >= k:
                for count_id in count[id]:
                    answer[id_list.index(count_id)] += 1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))