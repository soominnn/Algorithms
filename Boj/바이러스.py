from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
s = int(input())
connected = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(s):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

visited[1] = 1
queue = deque([1])
while queue:
    c = queue.popleft()
    for x in connected[c]:
        if visited[x] == 0:
            queue.append(x)
            visited[x] = 1
    
print(sum(visited) - 1)

# dfs 방식
# def dfs(v):
#     visited[v] = 1
#     for x in connected[v]:
#         if visited[v] == 0:
#             dfs(x)
# dfs(1)