import heapq
def solution(k, score):

    save, res = [], []
    for i in score:
        if len(save) < k:
            heapq.heappush(save,i)
        else:
            heapq.heappushpop(save,i)
        res.append(save[0])
    return res



print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
# print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))