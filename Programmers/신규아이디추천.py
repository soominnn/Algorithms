def solution(new_id):
    new_id = first_step(new_id)
    new_id = second_step(new_id)
    new_id = third_step(new_id)
    new_id = fourth_step(new_id)
    new_id = fifth_step(new_id)
    new_id = sixth_step(new_id)
    new_id = seventh_step(new_id)
    print(new_id)
    answer = new_id
    return answer

def first_step(new_id):
    return new_id.lower()

def second_step(new_id):
    example = ['-', '_', '.']
    for i in new_id:
        if i.isalpha() == False and i.isdigit() == False and i not in example:
            new_id = new_id.replace(i,'')
    return new_id
        
def third_step(new_id):
    stack = []
    for i in new_id:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1] and i == '.' and stack[-1] == '.':
                stack.pop()
                stack.append(i)
            else:
                stack.append(i)
    new_id = ''.join(stack)
    return new_id

def fourth_step(new_id):
    new_id = new_id.strip('.')
    return new_id
        
def fifth_step(new_id):
    if len(new_id) == 0:
        new_id = 'a'
    return new_id

def sixth_step(new_id):
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')
    return new_id

def seventh_step(new_id):
    if len(new_id) <= 2:
        count = 3 - len(new_id)
        for i in range(count):
            new_id += new_id[-1]
    return new_id