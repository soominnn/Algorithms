from itertools import combinations
from collections import defaultdict, deque

def solution(orders, course):
    cases = defaultdict(int)
    answer = [[] for _ in range(len(course))]
    result = set()
    course.sort()
    orders = sorted([list(order) for order in orders], key = lambda x : len(x))
    
    # 각 조합의 경우에 따라서 중복 카운트 해주기
    for num in course:
        for order in orders:
            for case in combinations(order, num):
                case = ''.join(sorted(case))
                cases[case] += 1

    # 각 경우들을 길이가 작은 case, 중복 카운트 수 오름차순으로 정렬해주기
    cases = sorted(cases.items(), key = lambda x: (len(x[0]), -x[1]))
    
    # 시간복잡도 줄이기 위한 deque 사용
    queue = deque(cases)
    max_value = cases[0][1]
    base_length = course[0]
    
    while queue:
        case = queue.popleft()
        length = len(case[0])
        cnt = case[1]
        if cnt >= 2:
            # 길이가 바뀌면 오름차순으로 정렬 해준 중복 카운트 수가 새로운 max_value값으로 변경됌
            if base_length != length:
                base_length = length
                max_value = cnt
            
            # 최빈값이 아니라면 pass 해주기
            if cnt != max_value:
                continue
            
            # 최빈값만 result에 문자열로 넣기
            result.add(''.join(sorted(case[0])))

    return sorted(result)