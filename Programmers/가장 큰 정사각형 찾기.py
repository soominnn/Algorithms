def solution(board):
    answer = 0 
    row, col = len(board), len(board[0])
    matrix = [[0] * (col + 1) for _ in range(row + 1)]
    
    for i in range(row):
        for j in range(col):
            matrix[i + 1][j + 1] = board[i][j]
            
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if matrix[i][j] != 0:
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                answer = max(answer, matrix[i][j])
                
    return answer * answer