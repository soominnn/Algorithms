from collections import deque

def bfs(map_info, start, end, n):
    queue = deque()
    queue.append(start)
    
    while queue:
        x = queue.popleft()
        if x == end:
            break
        
        for i in range(3):
            if i == 0:
                x_new = x * 3
            elif i == 1:
                x_new = x * 2
            else:
                x_new = x + n
        
            if x_new <= end:
                if map_info[x_new] == 0:
                    map_info[x_new] = map_info[x] + 1
                    queue.append(x_new)
    
    return map_info[end]

def solution(x, y, n):
    if x == y:
        return 0
    
    map_info = [0 for i in range(y + 1)]
    cnt = bfs(map_info, x, y, n)
    return cnt if cnt > 0 else -1

# dfs로 풀었을 때, 시간 초과
# def dfs(x, y, n, answer, count):
#     if x > y:
#         return
#     elif x == y:
#         answer.append(count)
#         return
   
#     dfs(x + n, y, n, answer, count + 1)
#     dfs(x * 2, y, n, answer, count + 1)
#     dfs(x * 3, y, n, answer, count + 1)

# def solution(x, y, n):
#     answer = []
#     dfs(x, y, n, answer, 0)
#     print(answer)
#     if len(answer) > 0:
#         return min(answer)
#     else:
#         return -1
