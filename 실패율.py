def solution(N, stages):
    length = len(stages)
    fail = {}
    answer = []
    for stage in range(1,N+1):
        if length != 0:
            fail[stage] = stages.count(stage)/length
            length -= stages.count(stage)
        else:
            fail[stage] = 0
    answer = sorted(fail, key = lambda x: fail[x], reverse = True)
    return answer