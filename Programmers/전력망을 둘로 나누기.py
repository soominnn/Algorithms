from itertools import combinations
from collections import deque

def bfs(start, wire, connected, visited, count):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for conn_node in connected[node]:
            if not visited[conn_node]:
                visited[conn_node] = True
                queue.append(conn_node)
                # 연결된 송전탑마다 카운트 해주기
                count += 1
                
    return count
    
def solution(n, wires):
    answer = n
    # 전선 한개를 끊은 경우의 수들 구하기
    for wire in combinations(wires, len(wires) - 1):
        connected = [[] for _ in range(n + 1)]
        # 전력망 연결 상태 구하기
        for s, e in wire:
            connected[s].append(e)
            connected[e].append(s)
        
        
        visited = [False] * (n + 1)
        
        for start in range(1, n + 1):
            if not visited[start]:
                # break 걸어준 이유는 전력망은 두개로 나누어지기 때문에 한번만 bfs로 한 영역을 구하면 끝이기 때문
                cnt = bfs(start, wire, connected, visited, 1)
                answer = min(answer, abs((n - cnt) - cnt))
                break
  
    return answer