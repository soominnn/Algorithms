def solution(n):
    prev_1 = bin(n)[2:].count('1')
    while True:
        n += 1
        next_1 = bin(n)[2:].count('1')
    
        if prev_1 == next_1:
            return n