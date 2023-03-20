N = int(input())
desert = [list(map(int, input().split())) for _ in range(N)]
answer = 0
now = [ N // 2, N // 2]
left = [(-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (-1, 0 ,0.07), (-1, 1, 0.01),
        (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
rate = {'left': left, 'right': right, 'down': down, 'up': up}

def move(cnt, dx, dy, direction):
    global answer
    for _ in range(cnt + 1):
        now[0], now[1] = now[0] + dx, now[1] + dy
        #경로 벗어나면 끝내기
        if now[0] < 0 or now[1] < 0:
            break

        spreads = 0
        for dx, dy, r in rate[direction]:
            nx, ny = now[0] + dx, now[1] + dy
            if r == 0:
                sand = desert[now[0]][now[1]] - spreads
            else:
                sand = int(desert[now[0]][now[1]] * r)
            
            if 0 <= nx < N and 0 <= ny < N:
                desert[nx][ny] += sand
            else:
                answer += sand
            spreads += sand

for i in range(N):
    if i % 2 == 0:
        move(i, 0, -1, 'left')
        move(i, 1, 0, 'down')
    else:
        move(i, 0, 1, 'right')
        move(i, -1, 0, 'up')

print(answer)