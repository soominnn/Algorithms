while True:
    sentence = input()
    if sentence == '.':
        break
    arr = []
    for s in sentence:
        if s == '(' or s == '[':
            arr.append(s)
        elif s == ')':
            if len(arr) > 0 and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(')')
                break
        elif s == ']':
            if len(arr) > 0 and arr[-1] == '[':
                arr.pop()
            else:
                arr.append('(')
                break
    
    if arr:
        print('no')
    else:
        print('yes')  