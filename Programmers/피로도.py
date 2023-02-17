from itertools import permutations

def solution(k, dungeons):
    orders = [i for i in range(len(dungeons))]
    answer = 0
    
    for order in list(permutations(orders, len(dungeons))):
        rem_fatigue = k
        count = 0
        for index in order:
            limit_fatigue = dungeons[index][0]
            fatigue = dungeons[index][1]
            if limit_fatigue <= rem_fatigue:
                rem_fatigue -= fatigue
                count += 1
                
        answer = max(answer, count)          
    
    return answer