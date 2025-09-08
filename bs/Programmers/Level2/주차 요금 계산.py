import datetime
import math


def get_fee(time, fees):
    return fees[1] + math.ceil(max(0, (time - fees[0])) / fees[2]) * fees[3]

def solution(fees, records):
    parking = {}
    total = {}
    for record in records:
        time, car, status = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)
        if status == 'IN': # 들어간 시간
            parking[car] = minutes
        # elif status == 'OUT': # 나온 시간 출차 - 입차
        #     #  a.get('name')
        #     if total.get(car):
        #         total[car] += minutes - total[car]
        #     else:
        #         total[car] = minutes - total[car]
        elif status == 'OUT':
            try:
                total[car] += minutes - parking[car]
            except:
                total[car] = minutes - parking[car]
            del parking[car] # 출차 차량 삭제

    for car, minute in parking.items():
        try:
            total[car] += 23 * 60 + 59 - minute
        except:
            total[car] = 23 * 60 + 59 - minute
    return [get_fee(time, fees) for car, time in sorted(list(total.items()), key=lambda x: x[0])] # 차량 번호순으로 정렬

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# "05:34 5961 IN",
# "06:00 0000 IN",
# "06:34 0000 OUT",
# "07:59 5961 OUT",
# "07:59 0148 IN",
# "18:59 0000 IN",
# "19:09 0148 OUT",
# "22:59 5961 IN",
# "23:00 5961 OUT"

# elif cmd == 'OUT':
# try:
#     stack[car] += minutes - parking[car]
# except:
#     stack[car] = minutes - parking[car]
# del parking[car] # 출차 차량 삭제