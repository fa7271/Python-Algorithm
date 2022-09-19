
def solution(A,B):
    # res = 0
    # for x, y in zip(A.sort(),B.sort(reverse=True)):
    #     res += x * y
    # return res
    return  sum([x*y for x, y in zip(sorted(A), sorted(B, reverse=True))])


print(solution([1, 4, 2],[4, 5, 4]))