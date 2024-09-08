import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(node):
    visited[node] = True
    for n in graph[node]:
        if not visited[n]:
            dfs(n)


visited = [False] * (n + 1)
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
