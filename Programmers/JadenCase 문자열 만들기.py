def solution(s):
    answer = ''
    s = list(s)
    index = 0
    while s:
        ch = s.pop(0)
        if index == 0 and ch.isalpha():
            answer += ch.upper()
            index += 1
        elif ch == " ":
            answer += " "
            index = 0
        else:
            answer += ch.lower()
            index += 1
        
    return answer