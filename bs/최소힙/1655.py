import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

import heapq
N = int(sys.stdin.readline())

leftHeap = [] # 최솟값 힙 중에 제일 큰 값
rightHeap = [] # 최댓값 힙 중에 제일 작은값
for i in range(N):
    n = int(sys.stdin.readline())
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -n)
    else:
        heapq.heappush(rightHeap, n)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        right = heapq.heappop(rightHeap)
        left = heapq.heappop(leftHeap)
        heapq.heappush(leftHeap, -right)
        heapq.heappush(rightHeap, -left)
    print(-leftHeap[0])
