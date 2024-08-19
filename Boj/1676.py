import math

n = int(input())
n_fac = math.factorial(n)

zero_cnt = 0
while n_fac % 10 == 0:
    n_fac //= 10
    zero_cnt += 1
print(zero_cnt)
