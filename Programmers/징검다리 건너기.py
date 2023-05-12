# mid 값은 건너갈 수 있는 사람의 수로, 이 값을 기준으로 이진 탐색
def solution(stones, k):
    left = 1
    right = max(stones)
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        # cnt : 연속으로 넘어갈 수 있는 디딤돌 cnt
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            # 연속이 끊기면 다시 카운트 하기
            else:
                cnt = 0
            
            # k개이상만큼 넘어갈 수 있다면 mid명 만큼 건너갈 수 없다는 뜻
            if cnt >= k:
                break
  
        if cnt >= k:
            right = mid - 1
   
        else:
            left = mid + 1
            
    return left