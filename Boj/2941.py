s = input()
cro = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']
cnt = 0
for i in range(len(cro)):
    cnt += s.count(cro[i])
    s = s.replace(cro[i],",")
for j in list(s):
    if j != ',':
        cnt+=1
print(cnt)
