import sys
from collections import deque

N = int(sys.stdin.readline())
space = []
for _ in range(N):
    space.append(list(map(int, sys.stdin.readline().split())))

size = 2
count = 0
time = 0
x = 0
y = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

#먹을 수 있는 물고기가 있는지 판단하는 함수    
def find_eat_possible(space):
    for i in range(len(space)):
        for j in range(len(space[0])):
            if 1 <= space[i][j] <= 6 and space[i][j] < size:
                return True
    return False

#처음 시작 위치 구하기
for i in range(len(space)):
    for j in range(len(space[0])):
        if space[i][j] == 9:
            x = i
            y = j
            
space[x][y] = 0

def find_near_fish(x, y):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque([[x, y, 0]])
    visited[x][y] = True
    cases = []
    while queue:
        x, y, distance = queue.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < N and 0 <= cy < N and not visited[cx][cy]:
                if space[cx][cy] <= size:
                    queue.append([cx, cy, distance + 1])
                    visited[cx][cy] = True
                    
                    if 1 <= space[cx][cy] <= 6 and space[cx][cy] < size:
                        cases.append([cx, cy, distance + 1])                
                    
    cases = sorted(cases, key = lambda x: (-x[2], -x[0], -x[1]))
    #가장 상단, 왼쪽 값 구하기
    if cases:
        return cases[-1]
    else:
        return [0, 0, 0] 

while find_eat_possible(space):
    x, y, distance = find_near_fish(x, y)
    if distance == 0:
        break

    #이동 거리만 큼 시간 더하기
    time += distance
    count += 1
    #자기 크기만큼 물고기 먹으면 size 커지기
    if count == size:
        count = 0
        size += 1

    #먹힌 물고기 공간 빈칸 만들기
    space[x][y] = 0

print(time)