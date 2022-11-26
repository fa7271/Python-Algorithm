import heapq
def solution(k, score):

    lst =[]
    heapq.heapify(lst)
    res = []
    for i in score:
        if len(lst) <k:
            heapq.heappush(lst,i)
            res.append(lst[0])
        else:
            x = heapq.heappop(lst)
            if i >= x:
                res.append(x)
                heapq.heappush(lst,i)
    print(res)
print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
# print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))