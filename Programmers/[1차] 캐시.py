def solution(cacheSize, cities):
    answer = 0
    cnt = 0
    lists = []
    orders = []
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    
    for city in cities:
        #소문자로 통일
        city = city.lower()
        
        if city in lists:
            orders[lists.index(city)] = cnt
            answer += 1
            
        else:
            if lists and len(lists) >= cacheSize:
                lists.remove(lists[orders.index(min(orders))])
                orders.remove(orders[orders.index(min(orders))])
            lists.append(city)
            orders.append(cnt)
            answer += 5
            
        cnt += 1
            
    return answer