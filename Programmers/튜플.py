def solution(s):
    result = []
    s = s.lstrip("{").rstrip("}").split("},{")
    s = sorted(s, key= lambda x: len(x))
    for i in s:
        isp = i.split(',')
        for j in isp:
            if int(j) not in result:  
                result.append(int(j))
    return result;