def solution(k, ranges):
    # 결과값들 구해놓고, 정적분 계산하기
    results = []
    kk = 0
    answer = []
    count = 0
    while k > 1:
        # 짝수면
        if k % 2 == 0:
            kk = k / 2
        # 홀수면
        else: 
            kk = k * 3 + 1
        
        results.append((k + kk) / 2)
        k = kk
        count += 1

    # 구간 계산
    for range in ranges:
        x1, x2 = range[0], range[1]
        x2 = count + x2
        if x1 <= x2:
            answer.append(sum(results[x1: x2]))
        else: 
            answer.append(-1)
     
    return answer
