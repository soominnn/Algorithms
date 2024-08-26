n, m = map(int, input().split())

cases = []


def dfs(start):
    if len(cases) == m:
        print(" ".join(map(str, cases)))
        return

    for i in range(start, n + 1):
        if i not in cases:
            cases.append(i)
            dfs(i + 1)
            cases.pop()


dfs(1)
