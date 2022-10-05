from itertools import permutations

#소수구하기
def prime(a):
    if a < 2:
        return 0
    elif a == 2:
        return 1
    else:
        #에라토스테네스의 체
        i = 2
        while i <= a / 2:
            if a % i == 0:
                return 0
            i += 1
        return 1
                
    
def solution(numbers):
    arr = []
    answer = 0
    
    #순열로 숫자들의 경우의 수 구해서 arr 리스트에 넣기
    for i in range(1, len(numbers)+1):
        data = permutations(numbers, i)
        for d in data:
            arr.append(int("".join(list(d))))
    #중복 제거
    arr = set(arr)

    for a in arr:
        answer += prime(a)

    return answer