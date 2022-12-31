def solution(s):
    count_2 = 0
    count_0 = 0
    
    while len(s) != 1:
        #0 제거
        len_s = len(s.replace('0', ''))
        #0 제거된 갯수 카운트
        count_0 += len(s) - len_s
        #2진법으로 변환
        s = bin(len_s)[2:]
        #이진 변환 횟수 카운트
        count_2 += 1
    
    return [count_2, count_0]