import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

import heapq

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

heap = list(map(int, sys.stdin.readline().rstrip().split(" ")))
heapq.heapify(heap)
for i in range(M):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    num = a + b
    heapq.heappush(heap, num)
    heapq.heappush(heap, num)
print(sum(heap))