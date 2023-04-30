import sys, heapq
input = sys.stdin.readline

N, E = map(int, input().split())
INF = int(1e9)
connected = [[] for _ in range(N + 1)]

for i in range(E):
    a, b, c = map(int, input().split())
    connected[a].append((b, c))
    connected[b].append((a, c))

v1, v2 = map(int, input().split())

def Dijkstra(start, end):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        wei, node = heapq.heappop(heap)
        if distance[node] < wei:
            continue
        for next_node, next_wei in connected[node]:
            total_wei = wei + next_wei
            if distance[next_node] > total_wei:
                distance[next_node] = total_wei
                heapq.heappush(heap, (total_wei, next_node))

    return distance[end]

#case1: 1 -> v1 -> v2 -> N
#case2: 1 -> v2 -> v1 -> N
path1 = Dijkstra(1, v1) + Dijkstra(v1, v2) + Dijkstra(v2, N)
path2 = Dijkstra(1, v2) + Dijkstra(v2, v1) + Dijkstra(v1, N)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))