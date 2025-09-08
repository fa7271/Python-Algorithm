def solution(schedules, timelogs, startday):
    # 출근 마감 시간 계산
    updated_schedules = []
    for i in schedules:
        total = str(i).zfill(4)  # 항상 네 자리로 맞추기
        hour = int(total[:-2])
        minute = int(total[-2:]) + 10

        if minute >= 60:
            hour += 1
            minute -= 60

        updated_schedules.append(hour * 100 + minute)

    res = len(schedules)

    for schedule, times in zip(updated_schedules, timelogs):
        for i, time in enumerate(times):
            day = (startday + i - 1) % 7

            if day >= 5:
                continue

            if time > schedule:
                res -= 1
                break

    return res


# print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809],
#                                   [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))
print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835],
                                      [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1))
