#큐
from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        
        answer.append(sec)
    
    return answer

#스택
def solution(prices):
    length = len(prices)

    answer = [i for i in range(length - 1, - 1, -1)]
    stack = []
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        
        stack.append(i)
    
    return answer 