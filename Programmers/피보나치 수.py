def solution(n):
    arr = [0, 1]
    for i in range(0, n):
        arr.append(arr[i] + arr[i + 1])

    return  arr[n] % 1234567