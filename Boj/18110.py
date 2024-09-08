import sys

n = int(sys.stdin.readline())


def roundUP(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)


if n == 0:
    print(0)
else:
    grades = []
    for _ in range(n):
        grades.append(int(sys.stdin.readline()))

    grades.sort()
    gap = roundUP(n * 0.15)

    grades = grades[gap : len(grades) - gap]

    print(roundUP(sum(grades) / len(grades)))
