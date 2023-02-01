def solution(triangle):
    answer = 0
    for index, row in enumerate(triangle):
        if len(row) >= 2:
            for idx in range(len(row)):
                if idx == 0:
                    triangle[index][0] += triangle[index - 1][0]
                elif idx == len(row) - 1:
                    triangle[index][-1] += triangle[index - 1][-1]
                else:
                    triangle[index][idx] += max(triangle[index - 1][idx - 1], triangle[index - 1][idx])
                
    return max(triangle[-1])