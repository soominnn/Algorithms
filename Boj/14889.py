def dfs(depth, idx):
    global min_diff
    if depth == n // 2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        
        min_diff = min(min_diff, abs(power1 - power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

n = int(input())
visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = 101

dfs(0, 0)
print(min_diff)


# 처음 조합으로 푼 풀이
# import sys
# from itertools import permutations
# n = int(sys.stdin.readline())
# index_cases = [i for i in range(n)]
# score_map = []
# answer = 101
# for _ in range(n):
#     score_map.append(list(map(int, sys.stdin.readline().split())))


# for start_team in permutations(index_cases, n // 2):
#     link_team = index_cases.copy()
#     for st in start_team:
#         link_team.remove(st)

#     start_team_score = 0
#     link_team_score = 0
#     for i in range(n // 2):
#         for j in range(n // 2):
#             if i != j:
#                 start_team_score += score_map[start_team[i]][start_team[j]]
#                 link_team_score += score_map[link_team[i]][link_team[j]]
   
#     answer = min(answer, abs(start_team_score - link_team_score))

# print(answer)