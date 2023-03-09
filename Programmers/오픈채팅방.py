def solution(record):
    dic = dict()
    answer = []
    for info in record:
        if len(info.split()) == 3:
            keyword, uid, name = info.split()
            dic[uid] = name

    for info in record:
        split_info = info.split()
        keyword, uid = split_info[0], split_info[1]
        name = dic[uid]
        if keyword == 'Enter':
            answer.append(f'{name}님이 들어왔습니다.')
        elif keyword == 'Leave':
            answer.append(f'{name}님이 나갔습니다.')
            
    return answer