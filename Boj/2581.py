def find_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())
mininum = 0;
total = 0;
first_check = True
for num in range(M, N + 1):
    if num < 2:
        continue
    elif num == 2:
        if first_check:
            first_check = False
            mininum = num
        total += num
    else:      
        if find_prime(num):
            if first_check:
                first_check = False
                mininum = num
            total += num
if total == 0:
    print(-1)
else:    
    print(total)
    print(mininum)
