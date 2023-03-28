def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for b in B:
        if b > A[0]:
            A.pop(0)
            answer += 1
    
    return answer