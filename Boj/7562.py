from collections import deque

def bfs():
    global x,y
    step = 0
    queue = deque()
    queue.append([x,y,step])
    visited[x][y] = 1
    while queue:
        x, y, step = queue.popleft()
        if x==dest_x and y==dest_y:
            return step
        for i in range(8):
            if 0<=x+dx[i]<l and 0<=y+dy[i]<l and visited[x+dx[i]][y+dy[i]] == 0:
                visited[x+dx[i]][y+dy[i]] = 1
                queue.append([x+dx[i],y+dy[i], step+1])

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]
n= int(input())
output = []
for i in range(n):
    count = 0
    l = int(input())
    visited = [[0 for _ in range(l)]for _ in range(l)] 
    x, y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    output.append(bfs())
print(*output, sep = "\n")
