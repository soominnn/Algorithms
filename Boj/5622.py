s = input()
arr = ['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
sum = 0 
for i in range(len(s)):
    for j in arr:
        if s[i] in j:
            sum += arr.index(j) + 3
print(sum) 
