from collections import deque
def bfs():
    n,k = map(int, input().split())
    visited = [0 for i in range(100001)]
    queue = deque()
    queue.append([n,0])
    while queue:
        x,y = queue.popleft()
        if x==k:
            return y 
        if x+1 <= k and visited[x+1] == 0:
            visited[x+1] = 1
            queue.append([x+1,y+1])
        if x-1 >= 0 and visited[x-1] == 0:
            visited[x-1] = 1
            queue.append([x-1,y+1])
        if x*2 <= 100000 and visited[x*2] == 0:
            visited[x*2] = 1
            queue.append([x*2,y+1])
print(bfs())