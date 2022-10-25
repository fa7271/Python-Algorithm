# def solution(order):
#     stact_left = []
#     stack_right =[]
#     i = 1
#     while True:
#         stact_left.append(i)
#         if stact_left[-1] == order[0]:
#             stack_right.append(order[i::])
#             break
#         i += 1
#     if stact_left ==[[]]:
#         stact_left.append(0)
#     elif stack_right == [[]]:
#         stack_right.pop()
#         stack_right.append('False')
#     now = 0
#     count = 0
#     while True:
#         if len(stact_left) == 0 or len(stack_right) == 0:
#             break
#         left, right = stact_left.pop(), stack_right.pop()
#         if order[now] == left:
#             count += 1
#             stack_right.append(right)
#             now += 1
#         elif order[now] == right:
#             count += 1
#             stact_left.append(left)
#             now += 1
#         else:
#             break
#     return count

# def solution(order):
    # count = 1
    # i = 0
    # while True:
    #     if order[i] - order[i+1] == 1 :
    #         count += 1
    #         order.pop(0)
    #         if len(order) == 1:
    #             break
    #     else:
    #         break
    #
    # return count

def solution(order):
    stacks = []
    i = 1
    idx = 0
    while i < len(order)+1:
        stacks.append(i)
        while stacks[-1] == order[idx]:
            idx += 1
            stacks.pop()
            if len(stacks) == 0:
                break
        i += 1


    return idx






# print(solution([5,4,3,2,1]))
print(solution([4,3,1,2,5]))