# arr = [1, 2, 3, 4]
# visited = [0] * len(arr)


# def permutations(n, new_arr):
#     global arr
#     if len(new_arr) == n:
#         print(new_arr)
#         return
#     for i in range(len(arr)):
#         if not visited[i]:
#             visited[i] = 1
#             permutations(n, new_arr + [arr[i]])
#             visited[i] = 0


# permutations(2, [])

# arr = [1, 2, 3, 4]


# def product(n, new_arr):
#     global arr
#     if len(new_arr) == n:
#         print(new_arr)
#         return
#     for i in range(len(arr)):
#         product(n, new_arr + [arr[i]])


# product(3, [])

arr = [1, 2, 3, 4]


def combinations(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i + 1)


combinations(2, [], 0)
