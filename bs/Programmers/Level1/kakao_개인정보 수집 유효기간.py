def solution(today, terms, privacies):

    dic = dict()
    for i in terms:
        Alpha, mon = i.split(" ")
        dic[Alpha] = int(mon)
    y,m,d = map(int,today.split("."))
    result = []
    for idx,i in enumerate(privacies,start=1):
        date, alpah = i.split(" ")
        yy,mm,dd = map(int,date.split("."))
        mm += int(dic[alpah])
        while mm > 12:
            yy += 1
            mm -= 12
        if yy > y:
            continue

        elif yy == y:
            if mm > m:
                continue

            elif mm == m:
                if dd > d:
                    continue

        result.append(idx)

    return result

#
# def solution(today, terms, privacies):
#
#     dic = dict()
#     for i in terms:
#         Alpha, mon = i.split(" ")
#         dic[Alpha] = mon
#     y,m,d = map(int,today.split("."))
#     sum_ymd = (y*12*28)+(m*28)+d
#     result =[]
#     for idx,i in enumerate(privacies,start=1):
#         date, alpah = i.split(" ")
#         yy,mm,dd = map(int,date.split("."))
#         mm += int(dic[alpah])
#         sum_ymd2 = (yy*12*28)+(mm*28)+dd
#         if sum_ymd2 <= sum_ymd:
#             result.append(idx)
    return result

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

#1. 텀을 딕셔너리 형태로 받아줌,
#2. 유효기간 하나씩 받고, 달을 더해줌
#3. 오늘이랑 비교함
#  2022 05 19 <= 2023 11 18 폐기 x
#  2022 05 19 >= 2021 05 18 폐기 0 0519 폐기
#  2022 05 19  2021 11 1
