n = int(input())
cnt = 0
for i in range(n+1):
    if i > 0 and i < 100:
        cnt = cnt + 1
    elif i >= 100:
        arr = list(str(i))
        if int(arr[1]) - int(arr[0]) == int(arr[2]) - int(arr[1]): 
            cnt = cnt+1
print(cnt)


