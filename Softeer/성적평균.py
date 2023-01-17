import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(K):
    A, B = map(int, sys.stdin.readline().split())
    total = 0
    for loc in range(A - 1, B):
        total += arr[loc]
    print(format(total / (B - A + 1), '.2f'))