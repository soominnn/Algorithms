def solution(citations):
    answer = 0
    for i in range(1, len(citations) + 1):
        cnt = 0
        for c in citations:
            if c >= i:
                cnt += 1
                
        if i >= cnt:
            answer = max(cnt, answer)
            
    return answer