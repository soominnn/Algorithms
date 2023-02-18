import heapq 

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while any(K > i for i in scoville):
        if len(scoville) <= 1:
            return -1
        low = heapq.heappop(scoville)
        second_low =heapq.heappop(scoville)
        total = low + second_low * 2
        heapq.heappush(scoville, total)
        answer += 1
        
    return answer