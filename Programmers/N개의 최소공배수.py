def solution(arr):
    answer = 2
    
    while True:
        key = 0
        for a in arr:
            if answer % a == 0:
                key += 1
                
        if key == len(arr):
            break
        
        answer += 1
        
    return answer