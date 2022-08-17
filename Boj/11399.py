n = int(input())
time = list(map(int, (input().split())))
sum = 0
tmp = 0 
while True:
    min = 1000
    if len(time) == 0:
        break
    for i in range(len(time)):
        if time[i] < min:
            min = time[i]
    tmp += min
    sum += tmp
    time.remove(min)
print(sum)