n = int(input())
triangle = [[0]]
for i in range(n):
    triangle.append(list(map(int,input().split())))
for i in range(n+1):
    for j in range(i):
        if i==1:
            continue
        if i==2:
            triangle[i][j] += triangle[i-1][0]
        else:
            if j==0:
                triangle[i][j] += triangle[i-1][0]
            elif j==i-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
print(max(triangle[n]))