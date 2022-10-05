from collections import deque

def bfs(start,maps,dx,dy):
    queue = deque([start])
    maps[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx == len(maps)-1 and ny == len(maps[0])-1:
                maps[nx][ny] = maps[x][y] + 1
                return
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                queue.append([nx,ny])
                maps[nx][ny] = maps[x][y] + 1
                
    

def solution(maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    answer = 0
    
    bfs([0,0], maps,dx,dy)
    
    if maps[len(maps)-1][len(maps[0])-1] == 1:
        answer = -1
    else:
        answer = maps[len(maps)-1][len(maps[0])-1]
    return answer