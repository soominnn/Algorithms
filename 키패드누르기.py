def find_num(btn,num):
    for x in range(4):
        for y in range(3):
            if btn[x][y] == num:
                numX = x
                numY = y
    return numX, numY
                    
def solution(numbers, hand):
    answer = ''    
    btn = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    pos_L_X = 3
    pos_L_Y = 0
    pos_R_X = 3
    pos_R_Y = 2
    for num in numbers:
        numX, numY = find_num(btn,num)
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            pos_L_X = numX
            pos_L_Y = numY
        if num == 3 or num == 6 or num == 9:
            answer += 'R'
            pos_R_X = numX
            pos_R_Y = numY
        if num == 2 or num == 5 or num == 8 or num == 0:
            l = abs(numX-pos_L_X)+abs(numY-pos_L_Y)
            r = abs(numX-pos_R_X)+abs(numY-pos_R_Y)
            if l < r:
                pos_L_X = numX
                pos_L_Y = numY
                answer += "L"
            if l > r:
                pos_R_X = numX
                pos_R_Y = numY
                answer += "R"
            if l == r:
                if hand == "right":
                    pos_R_X = numX
                    pos_R_Y = numY
                    answer += "R"
                else:
                    pos_L_X = numX
                    pos_L_Y = numY
                    answer += "L"
    return answer