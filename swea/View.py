def findMax(buildings, index):
    return max(buildings[index - 1], buildings[index - 2], buildings[index + 1], buildings[index + 2])

for i in range(1, 11):
    N = int(input())
    count = 0
    buildings = list(map(int, input().split()))
    for index in range(N):
        if 1 < index < N - 2:
                maxValue = findMax(buildings, index)
                if maxValue < buildings[index]:
                    count += buildings[index] - maxValue
    print(f'#{i} {count}')

        