from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        stack = []
        for ss in s:
            if stack:
                if ss == ')' and stack[-1] == '(':
                    stack.pop()
                elif ss == '}' and stack[-1] == '{':
                    stack.pop()
                elif ss == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(ss)
            else:
                stack.append(ss)
        if not stack:
            answer += 1 
        s.rotate(-1)
    
    return answer