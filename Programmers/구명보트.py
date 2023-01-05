from collections import deque

def solution(people, limit):
    boat = 0
    people.sort(reverse = True)
    queue = deque(people)

    while queue:
        high = queue.popleft()
        if queue and high + queue[-1] <= limit:
            queue.pop()
            boat += 1
        else:
            boat += 1
        
    return boat