from collections import Counter
import sys

n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
# 산술평균
mean = round(sum(numbers) / len(numbers))

print(mean)

# 중앙값
numbers.sort()
print(numbers[len(numbers) // 2])

# 최빈값
dic_numbers = Counter(numbers)
max_value = max(dic_numbers.values())
most_arr = []

for num, cnt in dic_numbers.items():
    if cnt == max_value:
        most_arr.append(num)


if len(most_arr) > 1:
    print(sorted(most_arr)[1])
else:
    print(most_arr[0])

# 범위
print(abs(max(numbers) - min(numbers)))
