t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    for j in range(n):
        tmp = zero
        zero = one
        one += tmp
    print(zero, one)