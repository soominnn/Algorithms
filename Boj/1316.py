n = int(input())
cnt = 0
for _ in range(n):
    s = list(input())
    for i in range(len(s)-2):
        if s[i] != s[i+1] and s[i] in s[i+2:]:
            cnt -=1
            break
    cnt += 1
print(cnt)
