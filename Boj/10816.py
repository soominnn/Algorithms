minus_cnt = [0 for _ in range(10000001)]
plus_cnt = [0 for _ in range(10000001)]

m = int(input())
list_m = list(map(int, input().split()))
for mm in list_m:
    if mm >= 0:
        plus_cnt[mm] += 1
    else:
        minus_cnt[abs(mm)] += 1

n = int(input())
list_n = list(map(int, input().split()))
for nn in list_n:
    if nn >= 0:
        print(plus_cnt[nn])
    else:
        print(minus_cnt[abs(nn)])
