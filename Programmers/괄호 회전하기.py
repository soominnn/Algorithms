def solution(s):
    answer = 0
    tmp = list(s)
    
    for _ in range(len(s)):
 
        stack = []
        for i in range(len(tmp)):
            if len(stack) > 0:
                if stack[-1] == '[' and tmp[i] == ']':
                    stack.pop()
                elif stack[-1] == '(' and tmp[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and tmp[i] == '}':
                    stack.pop()
                else:
                    stack.append(tmp[i])
            else:
                stack.append(tmp[i])
        if len(stack) == 0:
            answer += 1
        tmp.append(tmp.pop(0))
 
    return answer