import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)    
    answer = list(answer.keys())[0]
    return answer