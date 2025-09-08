import sys
import heapq

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
N = int(input())

heap = []
heapq.heapify(heap)
length = 0
for i in range(N):
    d, p = map(int, sys.stdin.readline().rstrip().split(" "))
    heapq.heappush(heap, (-d, p))
    length = max(p, length)
dist = [False] * (length + 1)
res = 0
while heap:
    x, y = heapq.heappop(heap)
    x = -x
    for idx in range(y, 0, -1):
        if not dist[idx]:
            dist[idx] = x
            res += x
            break
print(res)
