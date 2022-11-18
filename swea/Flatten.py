for i in range(10):
    dump = int(input())
    box = list(map(int, input().split()))
    box.sort()
    for _ in range(dump):
        box[box.index(min(box))] += 1
        box[box.index(max(box))] -= 1
    print(f'#{i + 1} {max(box) - min(box)}')