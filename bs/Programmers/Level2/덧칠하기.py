def solution(n, m, section):

    # pain_pan = [0] * n
    # for i in section:
    #     pain_pan[i-1] = 1
    #
    # left,right = section[0],section[-1]
    # count = right-left + 1
    # res = 0
    # while True:
    #     if count <= m:
    #         res += 1
    #         return res
    #     else:
    #         count -= m
    #         res += 1
    # return res

    paint, answer = section[0] , 0
    for i in section:
        if paint <= i:

            paint = i + m
            answer += 1
    return answer

print(solution(	8, 4, [2, 3, 6]))
# print(solution(	5, 4, [1, 3]))
# print(solution(4, 1, [1, 2, 3, 4]))
# print(solution(8, 2, [2, 6]))