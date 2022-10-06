def solution(brown, yellow):
    #갈색과 노란색 다 더하기
    total = brown + yellow
    for num in range(2,total):
        if total % num == 0 and num >= total // num:
            x = num
            y = total // num
            count = 0
            for i in range(x):
                for j in range(y):
                    if i != 0 and i != x-1 and j != 0 and j != y-1:
                        count += 1
            if count == yellow:
                return [x,y]
