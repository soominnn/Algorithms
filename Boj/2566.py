arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))
max_value = 0
index = [0, 0]
for i in range(9):
    for j in range(9):
        if max_value < arr[i][j]:
            max_value = arr[i][j]
            index[0] = i
            index[1] = j
print(max_value)
print(index[0] + 1, index[1] + 1)
    
