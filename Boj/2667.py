from collections import deque

#a
def bfs(village,dx, dy,x,y,n):
    village[x][y] = 0
    house_count = 1
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<n and village[x+dx[i]][y+dy[i]]==1:
                queue.append([x+dx[i],y+dy[i]])
                village[x+dx[i]][y+dy[i]] = 0        
                house_count += 1
    house.append(house_count)

n = int(input())
village = []
house = []
x=0
y=0
dx = [1,-1,0,0]
dy = [0,0,-1,1]
count = 0
for i in range(n):
    village.append(list(map(int,input())))

for i in range(n):
    for j in range(n):
        if village[i][j] == 1:
            bfs(village,dx,dy,i,j,n)
            count += 1
house.sort()
print(count)
if not house:
    print(0)
else:
    print(*house, sep = '\n')