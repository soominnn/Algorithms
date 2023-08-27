from collections import deque

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2

l = int(input())
turns = dict()
queue = deque()
queue.append((0, 0))

for _ in range(l):
    second, turn = input().split()
    turns[int(second)] = turn

x, y = 0, 0
board[x][y] = 1
cnt = 0
direction = 0


def turn(alphabet):
    global direction
    if alphabet == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]
    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if board[x][y] == 2:
        board[x][y] = 1
        queue.append((x, y))
        if cnt in turns:
            turn(turns[cnt])

    elif board[x][y] == 0:
        board[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        board[tx][ty] = 0
        if cnt in turns:
            turn(turns[cnt])

    else:
        break

print(cnt)
