n,m = map(int,input().split())
arr= [input() for _ in range(n)]
score=[]
for a in range(n-7):
    for b in range(m-7):
        case_w = 0
        case_b = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] != 'W':
                        case_w += 1
                    if arr[i][j] != 'B':
                        case_b += 1
                else:
                    if arr[i][j] != 'W':
                        case_b +=1
                    if arr[i][j] != 'B':
                        case_w += 1  
        score.append(case_w)
        score.append(case_b)
print(min(score))
