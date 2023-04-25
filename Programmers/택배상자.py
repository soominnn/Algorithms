from collections import deque

def solution(order):
    boxes = [i for i in range(1,len(order) + 1)]
    queue = deque(order)
    stack = []
    answer = 0
    o = queue.popleft()
    
    for box in boxes:
        if stack and o == stack[-1]:
            stack.pop()
            answer += 1
            o = queue.popleft()
            
        if box == o:
            answer += 1
            o = queue.popleft()
        else:
            stack.append(box)

    while queue:
        if stack and stack[-1] == o:
            stack.pop()
            answer += 1
            o = queue.popleft()
        else:
            break
            
    if o == stack[-1]:
        answer += 1
        
    return answer