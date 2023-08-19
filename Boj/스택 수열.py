n = int(input())
stack, ans, find = [], [], True

now = 1
for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        find = False
    
if find:
    for i in ans:
        print(i)
else:
    print('NO')