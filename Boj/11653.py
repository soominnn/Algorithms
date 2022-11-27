N = int(input())
num = 2
if N == 1:
    print()
else:
    while True:
        if N % num == 0:
            print(num)
            N = N // num
        else:
            num += 1
        if N == 1:
            break

