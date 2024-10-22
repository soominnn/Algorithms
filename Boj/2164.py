from collections import deque


cards = deque([i + 1 for i in range(int(input()))])
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])