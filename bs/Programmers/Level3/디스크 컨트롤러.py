import heapq
def solution(jobs):

    lst = sorted(jobs,key=lambda x:(x[1]))
    start = 0
    res = 0
    print(lst)
    while lst:
        for i in range(len(lst)):
            if lst[i][0] <= start:
                start += lst[i][1]
                res += start - lst[i][0]
                lst.pop(i)
                break
            if i == len(lst) - 1:
                start += 1

    return res // len(jobs)

import heapq
def solution1(jobs):
    answer, now, i = 0, 0, 0 # 답 시작 , 끝
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업들 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, (j[1], j[0]))
        print(heap)
        if heap:
            cur = heapq.heappop(heap)
            start = now # 시작값을 heap 에서 빼준걸로 바꿈
            now += cur[0] # 끝나는시간도 바꿔줌
            answer += now - cur[1] # 끝나는 시간 - 시작시간 빼줌
            i += 1
        else:
            now += 1
    return answer // i


# print(solution([[1,9], [0, 3], [4, 6]]))
# print(solution([[2,2], [3, 3], [5,5]]))
print(solution1([[1,9], [0, 3], [1,4],[1,5],[1,7],[2,2], [3, 3], [5,5]]))

# 3, 6 , 11 , 22 ,