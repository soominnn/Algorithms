import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline())
answer = 0
if arr[-1] == 'P':
    start = N - 1
    for i in range(start, 0, -1):
        if arr[i] == 'P':
            for j in range(K, -1 * K - 1, -1):
                if 0 <= i + j <= len(arr) - 1 and arr[i + j] == 'H':
                    arr[i + j] = 'z'
                    answer += 1
                    break

else:
    for i in range(len(arr)):
        if arr[i] == 'P':
            for j in range(-1 * K, K + 1):
                if 0 <= i + j <= len(arr) - 1 and arr[i + j] == 'H':
                    arr[i + j] = 'z'
                    answer += 1
                    break

print(answer)