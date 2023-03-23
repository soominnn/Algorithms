from itertools import permutations
import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
oper_counts = list(map(int, sys.stdin.readline().split()))
opers = []
for idx, oper_count in enumerate(oper_counts):
    for _ in range(oper_count):
        if idx == 0:
            opers.append('+')
        elif idx == 1:
            opers.append('-')
        elif idx == 2:
            opers.append('*')
        elif idx == 3:
            opers.append('//')

min_value = 1000000000
max_value = -1000000000

for oper_cases in list(permutations(opers, len(opers))):
    total = numbers[0]
    for i in range(len(oper_cases)):
        if oper_cases[i] == '+':
            total += numbers[i + 1]
        elif oper_cases[i] == '-':
            total -= numbers[i + 1]
        elif oper_cases[i] == '*':
            total *= numbers[i + 1]
        elif oper_cases[i] == '//':
            total = int(total / numbers[i + 1])

    min_value = min(min_value, total)
    max_value = max(max_value, total)

print(max_value)
print(min_value)
