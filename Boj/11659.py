import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i - 1]

for i in range(M):
    start, end = map(int, input().split())
    print(arr[end] - arr[start - 1])
