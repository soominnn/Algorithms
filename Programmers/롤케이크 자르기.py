from collections import Counter

def solution(topping):
    answer = 0
    chulsoo = set()
    topp_dict = Counter(topping)

    for topp in topping:
        if topp not in chulsoo:
            chulsoo.add(topp)
        
        topp_dict[topp] -= 1
        
        if topp_dict[topp] == 0:
            del topp_dict[topp]
            
        if len(topp_dict) == len(chulsoo):
            answer += 1

    return answer