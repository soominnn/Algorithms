N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()


def binary_search(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return 0


for b in B:
    print(binary_search(0, N - 1, A, b))
