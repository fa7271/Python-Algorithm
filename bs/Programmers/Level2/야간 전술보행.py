
def solution(distance, scope, times):
    list = [distance]
    for i in range(len(scope)):
        start, end = sorted(scope[i])
        work, rest = times[i]

        while start <= end:
            check = start % (work + rest) # 근무,휴식 패턴 파악하고
            if 0 < check and check <= work: # 남은 일수가 work 일수보다 낮으면 근무 인 날에 지나 간거다
                list.append(start) # 걸린 시간을 추가 해주고
                break   # 게임끝
            start += 1

    return sorted(list)[0]

# print(solution(10, [[3, 4], [5, 8]], [[2, 5], [4, 3]]))
print(solution(12, [[7, 8], [4, 6], [11, 10]], [[2, 2], [2, 4], [3, 3]]))