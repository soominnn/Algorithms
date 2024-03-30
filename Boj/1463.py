import sys
N = int(sys.stdin.readline())

dp =[0] * 1000001

# 연산 횟수 dp
for i in range(2, 1000001):
    # -1을 빼는 경우
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])