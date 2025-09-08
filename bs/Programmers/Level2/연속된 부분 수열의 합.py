from itertools import combinations
def solution(sequence, k):
    sum = 0
    end = 0
    res = []
    for i in range(len(sequence)):
        while sum < k and end < len(sequence):
            sum += sequence[end]
            end += 1
        if sum == k:
            res.append([ i, end-1,end-1-i ])
        sum -= sequence[i]

    res = sorted(res, key = lambda x:x[2])
    return res[0][:2]
# def solution2(sequence, k):
#     n = len(sequence)
#
#     max_sum = 0
#     end = 0
#
#     res = []
#     for i in range(n):
#
#         while max_sum < k and end < n:
#             max_sum += sequence[end]
#             end += 1
#
#         if max_sum == k:
#             res.append([i, end-1, end-1-i])
#
#         max_sum -= sequence[i]
#
#     res = sorted(res, key=lambda x: x[2])
#     return res[0][:2]





# print(solution(	[1, 2, 3, 4, 5,6,7,8,], 7))
print(solution(	[1, 1, 1, 2, 3, 4, 5], 5))
# print(solution([2, 2, 2, 2, 2], 6))