n = int(input())
for _ in range(n):
    arr = input()
    stack = []
    for a in arr:
        if a == ")" and len(stack) and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(a)
    if stack:
        print("NO")
    else:
        print("YES")
