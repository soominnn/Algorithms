T = int(input())
answer = ''
clap_case = ['3', '6', '9']
for num in range(1, T + 1):
    count = 0 
    for n in str(num):
        if n in clap_case:
            count += 1
    if count > 1:
        for _ in range(count):
            answer += '-' 
        answer += ' '
    elif count == 1:
        answer += '-' + ' '
    else: 
        answer += str(num) + ' '
print(answer)