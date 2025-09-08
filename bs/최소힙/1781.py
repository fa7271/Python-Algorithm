import sys
import heapq

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

lst = sorted([list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(N)], key=lambda x: (x[0]))
heap = []
for i in lst:
    heapq.heappush(heap, (i[1]))
    if len(heap) > i[0]:
        heapq.heappop(heap)

print(sum(heap))

