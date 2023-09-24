target = int(input())
n = int(input())
if n:
    broken = set(input().split())
else:
    broken = set()

ans = abs(100 - target)

for nums in range(1000001):
    for num in str(nums):
        if num in broken:
            break

    else:
        ans = min(ans, len(str(nums)) + abs(nums - target))

print(ans)
