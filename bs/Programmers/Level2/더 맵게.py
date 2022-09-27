# def solution(scoville, K):
#     sorted(scoville)
#     count = 0
#
#     while min(scoville) < int(K):
#         if scoville[0] < int(K) :
#             x = scoville.pop(0)
#             y = scoville.pop(0)
#             scoville.insert(0, x + (2*y))
#             count += 1
import heapq
def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K :
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
        count += 1
        if len(scoville) == 1 and scoville[0] < K :
            return -1
    return count


print(solution([4, 24, 3, 9, 10, 12], 7))

