num = int(input())
cnt = 1
while num > cnt:
    num -= cnt
    cnt += 1
if cnt % 2 == 0:
    print(num , '/' , cnt-num+1 , sep ='') 
else: 
    print(cnt-num+1, '/', num, sep = '')