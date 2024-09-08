n, k = map(int, input().split())

arr = list(range(1, n + 1))
start_idx = 0
res = []

for i in range(n):
    start_idx = (start_idx + k - 1) % len(arr)
    res.append(arr.pop(start_idx))

print("<" + str(res)[1:-1] + ">")
