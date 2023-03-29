import sys, math
A = int(sys.stdin.readline())
classrooms = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
answer = 0

for i in range(len(classrooms)):
    if classrooms[i] >= B:
        classrooms[i] -= B 
        answer += math.ceil(classrooms[i] / C) + 1
    else:
        answer += 1
        continue

print(answer)