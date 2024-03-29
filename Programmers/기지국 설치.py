from math import ceil

def solution(n, stations, w):
    answer = 0
    w_range = 2 * w + 1
    start = 1
    for station in stations:
        answer += max(ceil((station - w - start) / w_range), 0)
        start = station + w + 1
        
    if n >= start:
        answer += ceil((n - start + 1) / w_range)

    return answer