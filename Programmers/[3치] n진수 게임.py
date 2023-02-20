def convert(temp_case, rem):
    if rem == 10:
        temp_case.append('A')
    elif rem == 11:
        temp_case.append('B')
    elif rem == 12:
        temp_case.append('C')
    elif rem == 13:
        temp_case.append('D')
    elif rem == 14:
        temp_case.append('E')
    elif rem == 15:
        temp_case.append('F')
    else:
        temp_case.append(str(rem))
    
    return temp_case

def solution(n, t, m, p):
    answer = ''
    cases = []
    cnt = 0
    while len(cases) < t * m:
        temp_case = []
        rising_number = cnt
        
        #진법 변환
        while rising_number // n != 0:
            rem = rising_number % n
            temp_case = convert(temp_case, rem)   
            rising_number = rising_number // n
        
        temp_case = convert(temp_case, rising_number % n)
        #나머지의 역순으로 변경
        temp_case.reverse()
        cases += temp_case
        cnt += 1
    
    #원하는 크기만큼 자르기
    cases = cases[ : t * m]

    #튜브의 순서만 추출
    for case in enumerate(cases, 1):
        order, value = case
        if order % m == p or (order % m == 0 and m == p):
            answer += value

    return answer