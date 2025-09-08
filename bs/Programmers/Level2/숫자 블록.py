# def solution(begin, end):
#     lists = [0 for i in range(0, begin+1)]
#     lists.extend([0] * (end-begin))
#
#     for i in range(begin, end//2 + 1):
#         for j in list(range(i, end+1, i)):
#             if j == i:
#                 continue
#             else:
#                 lists[j] = i
#
#     return lists[begin:]

# def solution(begin, end):
#     answer = [0 for i in range(end+1)]
#     for i in range(end):  #0-9
#         for j in range(2,end): #2-9
#             if (i*j)>end:
#                 break
#             answer[i*j]=i
#         print(answer)
    # return list(answer.values())[begin-1:end+1]

- answer -
def solution (begin, end):
    list = []
    for i in range(begin, end+1):
        if i < 2:
            list.append(0)
        else:
            for j in range(2,int((i+1)**0.5) + 1):
                if i % j == 0 and i // j <= 10000000:
                    list.append(i // j)
                    break
            else:
                list.append(1)
    return list






print(solution(6,8))
# def a(x,n):
#     return list(range(x, x*n+1, x))
#
# print(a(2, 9))
