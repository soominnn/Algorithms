def solution(routes):
    answer = 1
    routes.sort(key = lambda x : (x[1], x[0]))
    base = routes[0][1]
    for route in routes:
        start, end = route
        if start <= base <= end:
            continue
        base = end
        answer += 1
        
    return answer