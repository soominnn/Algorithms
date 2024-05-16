def solution(sequence):
    answer = 0
    sequence2 = sequence[:]
    purse = 1
    
    for i in range(len(sequence)):
        sequence[i] *= purse
        purse *= -1
        sequence2[i] *= purse
    
    max_sum = 0 
    tmp = 0
    for s in sequence:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)
    
    tmp = 0
    for s in sequence2:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)
        
    answer = max_sum
    
    return answer