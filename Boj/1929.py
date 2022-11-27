def find_prime(num):
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True

M, N = map(int, input().split())

for num in range(M, N + 1):
    if num < 2:
        continue
    elif num == 2:
        print(num)
    else:      
        if find_prime(num):
            print(num)
           
