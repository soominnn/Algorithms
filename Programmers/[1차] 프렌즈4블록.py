def solution(m, n, board):
    board = [list(b) for b in board]
    answer = 0
    key = True
    while key:
        temp = []
        for i in range(m):
            for j in range(n):
                if i + 1 <= m - 1 and j + 1 <= n - 1:
                    if board[i][j] != '' and board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                        temp.append((i, j))
                        temp.append((i, j + 1))
                        temp.append((i + 1, j))
                        temp.append((i + 1, j + 1))

        if not temp:
            key = False
            
        temp = sorted(list(set(temp)), key = lambda x: (x[1], x[0]))
        answer += len(temp)
        for i, j in temp:
            board[i][j] = ''
            
        while True:
            move = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] != '' and board[i + 1][j] == '':
                        board[i + 1][j] = board[i][j]
                        board[i][j] = ''
                        move += 1
                        
            if move == 0:
                break

    return answer