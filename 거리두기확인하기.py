from collections import deque 

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(place, index):
    visited = [[0] * 5 for m in range(5)]
    queue = deque([index])
    while queue:
        x,y,d = queue.popleft()
        visited[x][y] = 1
        for p in range(4):
            vx = x + dx[p] 
            vy = y + dy[p]
            vd = d + 1
            if 0<=vx<=4 and 0<=vy<=4 and not visited[vx][vy]:
                if place[vx][vy] == 'P' and vd <= 2:
                    return 0
                if place[vx][vy] != 'X':
                    queue.append([vx,vy,vd])
    return 1
            
def solution(places):
    answer = []
    
    for place in places:
        key = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    res = bfs(place,[i,j,0])
                    if not res:
                        key = 0
        answer.append(key)
    return answer