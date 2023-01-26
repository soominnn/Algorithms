
def solution(clothes):
    answer = 1
    case = {}
    
    #옷 종류가 case에 있다면 appennd, 없다면 리스트로 추가하기
    for c in clothes:
        if c[1] in case.keys():
            case[c[1]].append(c[0])
        else:
            case[c[1]] = [c[0]]
    
    #각 종류별로 입을 수 있는 옷의 개수에 안 입는 경우 1을 더해서 그 값들을 모두 곱한다.
    for val in case.values():
        answer *= len(val) + 1
    
    #아무것도 안 입는 경우 빼기
    answer -= 1
    
    return answer 