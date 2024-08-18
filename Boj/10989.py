import sys

input = sys.stdin.readline

N = int(input())

cnt = [0] * 10001

for _ in range(N):
    cnt[int(input())] += 1

for i, c in enumerate(cnt):
    if c != 0:
        for _ in range(c):
            print(i)