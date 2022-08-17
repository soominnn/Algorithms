from itertools import permutations
n,m = map(int,input().split())
li = []
for i in range(n):
    li.append(i+1)
for i in permutations(li,m):
    print(*i)
