import heapq
def solution(n, works):
    work_sum = sum(works)
    if work_sum< n:
        return 0

    list = [-i for i in works]
    heapq.heapify(list)

    for i in range(n):
        x = heapq.heappop(list)
        x += 1
        heapq.heappush(list,x)

    return sum([i**2 for i in list])


    # for i in range(b):
    #     list[idx] += 1
    #     idx -= 1
    # return


# print(solution( 4, [4, 3, 3] ))
# print(solution( 1, [2, 1, 2] ))
print(solution( 3, [1, 1]))
