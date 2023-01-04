def solution(n, words):
    check_dup = []
    fail_number = 1
    fail_count = 1
    last_alphabet = words[0][0]
    
    for word in words:
        #이전에 나온 단어였는지 체크
        if word in check_dup:
            return [fail_number, fail_count]
        else:
            check_dup.append(word)
        
        #끝말잇기가 이어지는지 체크
        if last_alphabet == word[0]:
            last_alphabet = word[-1]
            if fail_number == n:
                fail_number = 1
                fail_count += 1
            else:
                fail_number += 1
        else:
            return [fail_number, fail_count]
            
    return [0, 0]