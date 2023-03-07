from collections import deque

def bfs(begin, target, words):
    visited = [False] * len(words)
    change = 0
    queue = deque([[begin, change]])

    while queue:
        base, change_value = queue.popleft()
        #target 찾으면 끝내기
        if base == target:
            return change_value
        
        split_base = list(base)
        #word의 인덱스도 맞춰서 1개 글자만 다른 지 확인하기
        for word in words:
            count = 0
            for index, sb in enumerate(split_base):
                if sb == word[index]:
                    count += 1

            if count == len(word) - 1 and visited[words.index(word)] == False:
                queue.append([word, change_value + 1])
                visited[words.index(word)] = True
    
    return 0

def solution(begin, target, words):
    return  bfs(begin, target, words)