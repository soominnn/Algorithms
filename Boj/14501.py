#DFS 방식
import sys
input = sys.stdin.readline

N = int(input())
work = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def consult(day, p_total):
    global answer
    if day == N:
        answer = max(answer, p_total)
        return

    t = work[day][0]
    p = work[day][1]

    if t + day <= N:
        consult(t + day, p_total + p)
    consult(day + 1, p_total)

for day in range(N):
    consult(day, 0)

print(answer)

#DP 방식
#bottom-up
import sys
N = int(input())
schedule = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

dp = [0 for _ in range(N + 1)]

for i in range(N):
    for j in range(i + schedule[i][0], N + 1):
        if dp[j] < dp[i] + schedule[i][0]:
            dp[j] = dp[i] + schedule[i][0]

print(dp[-1])

#top-down
N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N + 1)]

for i in range(N-1, -1, -1):
    if i + li[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], li[i][1] + dp[i + li[i][0]])

print(dp[0])