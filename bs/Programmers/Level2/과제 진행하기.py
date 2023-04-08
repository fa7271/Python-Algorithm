# def solution(plans):
#     lst = []
#     stack = []
#     res= []
#     plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])
#     print(plans)
#     for i in range(len(plans)):
#         sub, start, time = plans[i]
#         start =(60 * int(start[:2])) + int(start[3:])
#         lst.append([sub,start,int(time)])
#     lst = sorted(lst, key=lambda x: x[1])
#     print(lst)
#     while (len(lst) != 0 and stack != 0):
#         sub, start, time = lst.pop(0)
#         if start + time > lst[0][1]:
#             stack.append([sub, lst[0][1], time - (lst[0][1] - start)])
#
#         else:
#             res.append(sub)
#             if len(stack) != 0:
#                 a,b,c = stack.pop()
#                 b +=  lst[0][1] - (start+ time)
#                 c -= b

def solution(plans):
    answer = []
    plans = [[int(i[1][:2])*60+int(i[1][3:]),int(i[2]),i[0]] for i in plans]
    plans.sort()
    now, works = 0, []
    for i in plans:
        for j in range(len(works)):
            if works[j][1] == 0:
                continue
            elif i[0] >= now + works[j][1]:
                answer.append(works[j][2])
                now += works[j][1]
                works[j][1] = 0
            else:
                works[j][1] -= (i[0]-now)
                break
        works = [i] + works
        now = i[0]
    for i in works:
        if i[1] != 0:
            answer.append(i[2])
    return answer
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "30"]]))

# 1. stack = "music",750,30
# 2. stack =["music",750,30] ["computer", 750, 100]

