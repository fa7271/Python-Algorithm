def solution(ingredient):
    #
    # full =''
    # for i in ingredient:
    #     full = full + str(i)
    # count = 0
    # while '1231' in full:
    #     if '1231' in full:
    #         count += 1
    #         full = full.replace('1231','')
    # return count
    stack = []
    count = 0

    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            count += 1
            for i in range(4):
                stack.pop()
    return count

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
# print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))