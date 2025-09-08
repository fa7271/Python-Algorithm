import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque
import heapq
N = int(input())
lst =sorted([list(map(int,sys.stdin.readline().split())) for i in range(N)], key = lambda x:x[1])

hq = []
heapq.heappush(hq,lst[0][1])

for i in range(1,N):
    if lst[i][0] >= hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq,lst[i][1])
print(hq)
print(len(hq))