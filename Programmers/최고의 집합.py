def solution(n, s): 
    answer = [s // n] * n
    rem = s % n
    index = n - 1
    
    if n > s:
        return [-1]
    
    #맨 뒤 값부터 1씩 더해주면서 늘리기
    while rem > 0:
        answer[index] += 1
        rem -= 1
        index -= 1
        if index == 0:
            index = n - 1
        
    return answer