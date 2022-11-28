def find_prime(num):
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True

arr = list(range(2, 246912))
store = []

for a in arr:
    if a < 2:
        continue
    elif a == 2:
        store.append(a)
    else:      
        if find_prime(a):
            store.append(a)

while True:
    count = 0
    n = int(input())
    # n은 0일때 끝내기
    if n == 0:
        break
    for i in store:
        if n < i <= 2 * n:
            count += 1
    print(count)