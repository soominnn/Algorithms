from collections import deque

def bfs(maps, visited, loc, total):
    queue = deque([loc])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[loc[0]][loc[1]] = True
    total = int(maps[loc[0]][loc[1]])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < len(maps) and 0 <= cy < len(maps[0]) and not visited[cx][cy]:
                queue.append([cx, cy])
                # 상하좌우 연결되있는 섬들의 숫자 합하기
                total += int(maps[cx][cy])
                visited[cx][cy] = True
                
    return total
                
    
def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    # X표시대로 visited 설정해주기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X':
                visited[i][j] = True
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(maps, visited, [i, j], 0))
    
    return sorted(answer) if answer else [-1] 