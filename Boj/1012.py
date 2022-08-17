from collections import deque

def BFS(arr, M, N, x, y):
    arr[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            if 0<=x+dx[i]<M and 0<=y+dy[i]<N and arr[x+dx[i]][y+dy[i]] == 1:
                queue.append([x+dx[i],y+dy[i]])
                arr[x+dx[i]][y+dy[i]] = 0 

T = int(input())
count_arr = []
for _ in range(T):
    count = 0 
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(K):
        ix,iy = map(int, input().split())
        arr[ix][iy] = 1
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                BFS(arr, M, N, i, j)
                count += 1
    count_arr.append(count)
print(*count_arr, sep = '\n')