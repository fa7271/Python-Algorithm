# def solution(L, x):
#     answer = []
#     if x in L:
#         for idx, el in enumerate(L):
#             if el == x:
#                 answer.append(idx)
#     if x not in L:
#         answer.append(-1)
#     return answer


def solution(L, x):
    if x in L:
        x = [i for i, y in enumerate(L) if y == x]
    else:
        return [-1]

solution([64, 72, 83, 72, 54], 49)


# def solution(L, x):
#     if x in L:
#         return [i for i, y in enumerate(L) if y == x]
#     else:
#         return [-1]
