def solution(progresses, speeds):

    answer = []
    day = 0
    count = 0

    while len(progresses) > 0 :
        if ( progresses[0] + day * speeds[0] ) >= 100 :     # 100% 이상이면
            progresses.pop(0)                               # 리스트와
            speeds.pop(0)                                   # 속도 삭제한 후
            count += 1                                      # 배포 개수 1 증가
        else :
            if count > 0 :                                  # 100% 이상이 아닌데, 앞에서 배포할 작업이 있다면
                answer.append(count)                        # 배포개수를 answer 리스트에 담아준 후
                count = 0                                   # count 초기화
            day += 1                                        # 다음 날짜 작업을 확인하기 위해 작업 일수에 하루를 더해줌
    answer.append(count)                                    # 마지막 날꺼 더해줌

    return answer
print(solution(	[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# print(solution([93, 30, 55], [1, 30, 5]))
# 5 10 1 1 20 1

