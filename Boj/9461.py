import sys

input = sys.stdin.readline
T = int(input())
answer = []
for i in range(T):
    tc = int(input())
    if tc <= 3:
        answer.append(1)
        continue
    elif tc <= 5:
        answer.append(2)
        continue

    triangle = [0] * tc
    triangle[0], triangle[1], triangle[2], triangle[3], triangle[4] = 1, 1, 1, 2, 2

    for i in range(5, tc):
        triangle[i] = triangle[i - 1] + triangle[i - 5]
    answer.append(triangle[tc - 1])

print(*answer, sep = '\n')