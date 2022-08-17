num = int(input())
li = []
cnt = 666
key = 0 
while True:
    li.append(str(cnt))
    if li[-1].count('666') >= 1:
        key += 1
    if key == num:
        break
    cnt += 1
print(cnt)     

