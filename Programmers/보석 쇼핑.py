def solution(gems):
    answer = [0, len(gems) - 1]
    size = len(set(gems))
    start, end = 0, 0
    gems_dict = dict()
    gems_dict[gems[0]] = 1
    
    while start < len(gems) and end < len(gems):
        if len(gems_dict) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            else:
                gems_dict[gems[start]] -= 1
                if gems_dict[gems[start]] == 0:
                    del gems_dict[gems[start]]
                start += 1
        
        else:
            end += 1
            if end == len(gems):
                break
                
            if gems[end] in gems_dict:
                gems_dict[gems[end]] += 1
            else:
                gems_dict[gems[end]] = 1
    
    return [answer[0] + 1, answer[1] + 1]

# def solution(gems):
#     start = 1
#     end = 1
#     length = len(gems)
#     set_length = len(set(gems))
#     answer = [1, length]
#     gems.insert(0, '0')

#     while end <= length and start <= length:
#         cnt = len(set(gems[start: end + 1]))
#         if cnt == set_length:
#             if answer[1] - answer[0] > end - start:
#                 answer = [start, end]
#             start += 1
#         elif cnt > set_length:
#             start += 1
#         elif cnt < set_length:
#             end += 1
        
#     return answer