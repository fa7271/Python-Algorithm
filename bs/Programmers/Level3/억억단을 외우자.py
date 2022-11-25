from collections import deque, Counter
from itertools import islice

#
# def solution(e, starts):
#     lst = deque([(i, e) for i in starts])
#     dic = {x:0 for x in range(1,e+1)}
#     res = []
#     while lst:
#         left, right = lst.popleft()
#         for x in range(left, right+1):
#             count = 0
#             for i in range(1, int(x**0.5)+1):
#                 if x % i == 0:
#                     count += 1
#                     if i ** 2 != x:
#                         count += 1
#             dic[x] = count
#
#         arr = dict(islice(dic.items(),left-1,right))
#         max = Counter.most_common(arr,1)
#         res.append(max)
#
#     return [x for x,y in sum(res,[])]

    # x = sorted(dic.items(), key=lambda x:x[1])

    # start, ex = 0, len(starts)
    # while ex != 0:
    #     arr = dict(islice(dic.items(),starts[start],e))
    #     ex -= 1
    #     start += 1
    #     res += Counter.most_common(arr,1)
    # return [x for x,y in res]


# def solution(e, starts):
#     lst = deque([(i, e) for i in starts])
#
#     dic = {x:0 for x in range(1,e+1)}
#     res = []
#     for i in range(2,e+1):
#         if dic[i] == 0:
#             dic[i] = 'sosu'
#             for j in range(2*i, e+1,i):
#                 dic[j] = 2
#     print(dic)
#     for z in range(min(starts), e+1):
#         for x in range(z, e+1):
#             count = 0
#             for i in range(1, int(x**0.5)+1):
#                 if x % i == 0:
#                     count += 1
#                     if i ** 2 != x:
#                         count += 1
#             if dic[x] != 2:
#                 dic[x] = count
#     for i in starts:
#         arr = dict(islice(dic.items(),i-1,e))
#         max = Counter.most_common(arr,1)
#         res.append(max)
#
#     return [x for x,y in sum(res,[])]

def solution(e, starts):

    lst = [1 for _ in range(e+1)]
    for a in range(2, e+1) :
        for b in range(a, e+1, a) :
            lst[b] += 1
    result = []
    idx = len(lst)-1 # 8 인덱스 8
    max_value = lst[-1]
    for i in range(idx ,0 ,-1):
        print(lst)
        if lst[i] >= max_value:
            idx = i
            max_value = lst[i]
        lst[i] = idx
    for i in starts:
        result.append(lst[i])

    return result


    # for i in starts:
    #     arr = dict(islice(dic.items(),i-1,e))
        # print(arr)
        # max = Counter.most_common(arr,1)
        # res.append(max)
    # return [x for x,y in sum(res,[])]

# print(solution(50, [10, 21, 40]))
print(solution(10,[3,1,7]))


def solution2(e, starts):
    answer = []
    data = [1] * (e + 1)

    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            data[j] += 1
    arr = [0 for _ in range(e + 1)]
    max_val = data[-1]


    idx = len(data) - 1
    for i in range(len(data) - 1, 0, -1):
        if data[i] >= max_val:
            idx = i
            max_val = data[i]
        arr[i] = idx
print(solution2(8,[3,1,7]))
