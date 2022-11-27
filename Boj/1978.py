def find_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

N = int(input())
arr = list(map(int, input().split()))
count = 0
for a in arr:
    if a < 2:
        continue
    elif a == 2:
        count += 1
    else: 
        if find_prime(a):
            count += 1
print(count)