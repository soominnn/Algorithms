from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    speed_queue = deque(speeds)
    cnt = 0
    while queue:
        if queue[0] >= 100:
            queue.popleft()
            speed_queue.popleft()
            cnt += 1
            
            if not queue:
                answer.append(cnt)
                
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
                
            for i in range(len(queue)):
                queue[i] += speed_queue[i]

    return answer