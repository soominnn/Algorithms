def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
        

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)

# 조합 풀이 시간 초과
# from itertools import combinations

# def solution(number, k):
#     answer = 0
#     for value in combinations(list(number), len(number) - k):
#         answer = max(answer, int(''.join(value)))
#     return str(answer)