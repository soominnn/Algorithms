from collections import deque

def bfs(box,M,N,one_stack):
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    count = 0
    queue = deque()
    for tmp in one_stack:
        queue.append([tmp[0],tmp[1]])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<M and box[x+dx[i]][y+dy[i]] == 0:
                box[x+dx[i]][y+dy[i]] = box[x][y] + 1
                queue.append([x+dx[i],y+dy[i]])
                count = box[x][y]    
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                count = -1
                return(count)
    return(count)

M,N = map(int,input().split())
box = []
for i in range(N):
    box.append(list(map(int, input().split())))
one_stack = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            one_stack.append([i,j])
print(bfs(box,M,N,one_stack))
