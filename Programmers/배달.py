import heapq

INF = int(1e9)

def Dikstra(start, connected, distance):
    heap = []
    heapq.heappush(heap, (start, 0))
    while heap:
        node, wei = heapq.heappop(heap)
        if distance[node] < wei:
            continue
        for next_node, next_wei in connected[node]:
            total_wei = wei + next_wei
            if distance[next_node] > total_wei:
                distance[next_node] = total_wei
                heapq.heappush(heap, (next_node, total_wei))
    
    return distance
    

def solution(N, road, K):
    answer = 0
    connected = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    distance[1] = 0
    
    for f, b, d in road:
        connected[f].append((b, d))
        connected[b].append((f, d))
    
    distance = Dikstra(1, connected, distance)

    for d in distance:
        if 0 <= d <= K:
            answer += 1
            
    return answer