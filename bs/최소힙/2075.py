import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
import heapq

heap = []

n = int(input())
graphs = [list(map(int,sys.stdin.readline().split(" "))) for _ in range(n)]
for graph in graphs:
    for number in graph:
        if len(heap) < n:
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])

# heap = [-graph[x][y] for x in range(n) for y in range(n)]
# heapq.heapify(heap)
# for i in range(n-1):
#     heapq.heappop(heap)
# print(-heapq.heappop(heap))

