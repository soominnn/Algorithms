from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    while queue:
        front = queue.popleft()
        answer += 1
        for q in queue:
            if front < q:
                queue.append(front)
                if location == 0:
                    location = len(queue)
                answer -= 1
                break
 
        location -= 1
        if location < 0:
            return answer


