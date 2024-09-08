import sys

arr = set()
m = int(sys.stdin.readline())
for _ in range(m):
    order = sys.stdin.readline().strip().split()
    if len(order) > 1:
        order, n = order[0], int(order[1])
    else:
        order = order[0]

    if order == 'add':
        arr.add(n)

    elif order == 'check':
        if n in arr:
            print(1)
        else:
            print(0)

    elif order == 'remove':
        arr.discard(n)

    elif order == 'toggle':
        if n in arr:
            arr.discard(n)
        else:
            arr.add(n)

    elif order == 'all':
        arr = set([i for i in range(1, 21)])

    elif order == 'empty':
        arr = set()