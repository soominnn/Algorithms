from collections import deque

def bfs(visited, start, computer, n):
    visited[start] == True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for i in computer[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

n = int(input())
s = int(input())
visited = [False]*(n+1)
computer = [[] for i in range(n+1)]
for i in range(s):
    tmp = list(map(int,input().split()))
    computer[tmp[0]].append(tmp[1])
    computer[tmp[1]].append(tmp[0])
bfs(visited, 1, computer, n)
print(visited.count(True)-1)

