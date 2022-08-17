from collections import deque
import copy
#dfs
def dfs(node,v,visited):
    if visited[v] == True:
        return
    visited[v] = True
    print(v, end = ' ')
    for i in node[v]:
        dfs(node,i,visited)
             
#bfs 
def bfs(node, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in node[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n,m,v = map(int, input().split())
node = [[] for i in range(n+1)]
visited = [False]*(n+1)
for i in range(m):
    tmp = list(map(int,input().split()))
    node[tmp[0]].append(tmp[1])
    node[tmp[1]].append(tmp[0])
for i in range(n+1):
    node[i].sort()

node2 = copy.deepcopy(node)
v2 = copy.deepcopy(v)
visited2 = copy.deepcopy(visited)

dfs(node,v,visited)
print()
bfs(node2,v2,visited2)
