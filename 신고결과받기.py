from collections import defaultdict

def solution(id_list, report, k):
    x_list = defaultdict(set)
    y_list = defaultdict(set)
    answer = []

    for i in range(len(report)):
        x,y = report[i].split()
        x_list[x].add(y)
        y_list[y].add(x)

    for name in id_list:
        count = 0
        for defendant in x_list[name]:
            if len(y_list[defendant]) >= k:
                count+=1
        answer.append(count)

    return answer