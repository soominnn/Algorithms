from itertools import combinations

def solution(word):
    cases = ['A', 'E', 'I', 'O', 'U'] * 5
    dic = []

    for i in range(1, 6):
        for case in list(combinations(cases, i)):
            dic.append(''.join(case))

    dic = sorted(list(set(dic)))

    return dic.index(word) + 1