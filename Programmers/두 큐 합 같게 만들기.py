from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    answer = 0
    cnt = 0
    cnt_limit = (len(queue1) + len(queue2)) * 2
    
    while True:
        if cnt >= cnt_limit:
            answer = -1
            break
            
        if q1_sum < q2_sum:
            item = queue2.popleft()
            queue1.append(item)
            q1_sum += item
            q2_sum -= item
            answer += 1
            cnt += 1
            
        elif q1_sum > q2_sum:
            item = queue1.popleft()
            queue2.append(item)
            q2_sum += item
            q1_sum -= item
            answer += 1
            cnt += 1
            
        # 두 큐의 합이 같다면
        else:
            break
    
    return answer