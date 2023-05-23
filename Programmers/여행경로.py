from collections import defaultdict

def solution(tickets):
    answer = []
    path = defaultdict(list)
    for ticket in tickets:
        path[ticket[0]].append(ticket[1])
    
    for key in path.keys():
        path[key].sort(reverse = True)

    stack = ['ICN']
    while stack:
        top = stack[-1]
        # 길이 끝기는 경우 조건
        if not path[top]:
            answer.append(stack.pop())
        else:
            stack.append(path[top].pop())
    
    answer.reverse()
    return answer
            
# 오답1 - BFS
# from collections import deque

# def bfs(tickets):
#     queue = deque(['ICN'])
#     answer = ['ICN']
#     while queue:
#         start = queue.popleft()
        
#         for idx, ticket in enumerate(tickets):
#             if ticket[0] == start:
#                 answer.append(ticket[1])
#                 queue.append(ticket[1])
#                 tickets.pop(idx)
#                 break
    
#     return answer
                
# def solution(tickets):
#     tickets.sort(key = lambda x : x[1])
    
#     return bfs(tickets)

# 오답2 - DFS
# import copy

# def dfs(start, tickets, arr, cnt, limit):
#     if cnt == limit:
#         return arr
    
#     for idx, ticket in enumerate(tickets):
#         if ticket[0] == start:
#             arr.append(ticket[1])
#             tickets.pop(idx)
#             dfs(ticket[1], tickets, arr, cnt + 1, limit)

#     return arr
    
# def solution(tickets):
#     tickets.sort(key = lambda x : x[1])
#     total_tickets = set([])
#     for ticket in tickets:
#         total_tickets.add(ticket[0])
#         total_tickets.add(ticket[1])

#     return dfs('ICN', tickets, ['ICN'], 1, len(tickets) + 1)