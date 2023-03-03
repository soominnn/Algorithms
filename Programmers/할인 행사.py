from collections import Counter

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - 9):
        count = [0] * len(want)
        #10개씩 자르기
        cases = discount[i : i + 10]
        
        for case in cases:
            if case in want:
                count[want.index(case)] += 1
        
        if count == number:
            answer += 1
            
    return answer