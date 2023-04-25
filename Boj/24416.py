n = int(input())
re_cnt = 1

def re(n):
    global re_cnt
    if n == 1 or n == 2:
        return 1
    else:
        re_cnt += 1
        return re(n - 1) + re(n - 2)

def dp(n):
    cnt = 0
    nums = [0] * (n + 1)
    nums[1] = nums[2] = 1
    for i in range(3, n + 1):
        cnt += 1
        nums[i] = nums[i - 1] + nums[i - 2]
    return cnt

re(n)
cnt = dp(n)
print(re_cnt, cnt)
