import heapq
def solution(x):
    nums = [1,5,4,8,7,3]
    heap = []
    for i in nums:
        # heapq.heappush(heap , (-i,i))
        heapq.heappush(heap , (-i,i))
    while heap:
        print(heapq.heappop(heap))


    #      1  ---> root 이런느낌
    #    /   \
    #   3     5
    #  / \   /
    # 4   8 7