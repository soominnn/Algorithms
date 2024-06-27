def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            # 해당 심사대에서 주어진 시간동안 심사 받은 수 구하기
            people += mid // time

            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
