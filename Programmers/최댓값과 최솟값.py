def solution(s):
    case = list(map(int, s.split()))
    answer = ''
    answer += str(min(case))
    answer += ' '
    answer += str(max(case))
    return answer