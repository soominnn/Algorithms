import sys, copy
from collections import deque

N, M = map(int, sys.stdin.readline().split())
virus_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1 ,0, 0]
dy = [0, 0, 1, -1]
max_count = 0

def bfs(virus_map):
    queue = deque([])
    rep_virus_map = copy.deepcopy(virus_map)
    for i in range(N):
        for j in range(M):
            if virus_map[i][j] == 2:
                queue.append([i, j])
    
    while queue:
        x, y = queue.popleft()
        for c in range(4):
            cx = x + dx[c]
            cy = y + dy[c]
            if 0 <= cx < N and 0 <= cy < M and rep_virus_map[cx][cy] == 0:
                rep_virus_map[cx][cy] = 2
                queue.append([cx, cy])
 
    count = 0
    for ii in range(N):
        for jj in range(M):
            if rep_virus_map[ii][jj] == 0:
                count += 1
                
    global max_count
    max_count = max(max_count, count)

def make_wall(cnt):
    if cnt == 3:
        bfs(virus_map)
        return
                    
    for i in range(N):
        for j in range(M):
            if virus_map[i][j] == 0:
                virus_map[i][j] = 1
                make_wall(cnt + 1)
                virus_map[i][j] = 0

make_wall(0)
print(max_count)