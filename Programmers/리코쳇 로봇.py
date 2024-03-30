from collections import deque

def solution(board):
    r = len(board)
    c = len(board[0])
    sx, sy = 0, 0 
    
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                sx, sy = i, j
    
    def bfs():
        queue = deque()
        queue.append([sx, sy])     
        
        visited = [[0] * c for _ in range(r)]
        visited[sx][sy] = 1
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        while queue:
            px, py = queue.popleft()
            
            if board[px][py] == 'G':
                return visited[px][py]
            
            for i in range(4):
                nx, ny = px, py
                while True:
                    nx, ny = nx + dx[i], ny + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                        
                    if 0 > nx or nx >= r or 0 > ny or ny >= c:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[px][py] + 1
                    queue.append([nx, ny])
        return -1
            
    answer = bfs()
    return answer-1 if answer > 0 else -1