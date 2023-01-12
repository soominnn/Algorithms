def solution(lottos, win_nums):
    zero_cnt = 0
    win_cnt = 0
    answer1 = 0
    answer2 = 0 

    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
        else:
            if lotto in win_nums:
                win_cnt += 1
                win_nums.remove(lotto)

    if zero_cnt <= len(win_nums):
        max_hit = win_cnt + zero_cnt
        min_hit = win_cnt
    else:
        max_hit = win_cnt + len(win_nums)
        min_hit = win_cnt

    if 7 - max_hit == 7:
        answer1 = 6
    else:
        answer1 = 7 - max_hit

    if 7 - min_hit == 7:
        answer2 = 6
    else:
        answer2 = 7 - min_hit

    return [answer1, answer2]