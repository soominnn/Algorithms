def solution(arr):
    count = [0, 0]
    length = len(arr)
    
    def dfs(length, x, y):
        base = arr[x][y]
        for i in range(x, x + length):
            for j in range(y, y + length):
                if base != arr[i][j]:
                    ll = length // 2
                    dfs(ll, x, y)
                    dfs(ll, x + ll, y)
                    dfs(ll, x, y + ll)
                    dfs(ll, x + ll, y + ll)
                    return
                
        count[base] += 1
    dfs(length, 0, 0)
    return count