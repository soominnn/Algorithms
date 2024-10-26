import sys

input = sys.stdin.readline
n, m = map(int, input().split())
memo = {}
for _ in range(n):
    address, pwd = input().split()
    memo[address] = pwd


for _ in range(m):
    find_add = input().rstrip()
    print(memo[find_add])
