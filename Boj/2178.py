from collections import deque

def bfs(miro,N,M):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append([1,1])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            if 1<=x+dx[i]<=N and 1<=y+dy[i]<=M and miro[x+dx[i]][y+dy[i]] == 1:
                queue.append([x+dx[i],y+dy[i]])
                miro[x+dx[i]][y+dy[i]] = miro[x][y] + 1
    return miro[N][M]

N,M = map(int,input().split())
miro =[[0 for _ in range(M+1)]]
for i in range(N):
    miro.append(list(map(int, '0' + input())))
print(bfs(miro,N,M))
