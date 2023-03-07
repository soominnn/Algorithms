def solution(m, n, puddles):
    hometown = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    hometown[1][1] = 1
    
    for row, col in puddles:
        hometown[col][row] = -1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if hometown[i][j] == -1:
                hometown[i][j] = 0
            else:
                hometown[i][j] += hometown[i - 1][j] + hometown[i][j - 1]

    
    return hometown[n][m] % 1000000007