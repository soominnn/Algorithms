def solution(msg):
    answer = []
    dic = dict()
    for c in range(ord('A'), ord('Z') + 1):
        dic[chr(c)] = c - ord('A') + 1
    idx = 27
    start, end = 0, 1

    while end < len(msg) + 1:
        find = msg[start: end]
        if find in dic:
            end += 1
        else:
            answer.append(dic[find[ : -1]])
            dic[find] = idx
            idx += 1
            start = end - 1
    
    answer.append(dic[find])
    return answer