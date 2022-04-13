def solution(board, moves):
    board = [[0]* len(board)] + board
    for row_first in range(len(board)):
        board[row_first].insert(0,0)  
    answer = 0
    basket = []
    for col in moves:
        for row in range(len(board)):
            if board[row][col] != 0:
                basket.append(board[row][col])
                if len(basket) >= 2 and basket[-1] == basket[-2]:
                    basket.pop() 
                    basket.pop()
                    answer += 2
                board[row][col] = 0
                break
    return answer