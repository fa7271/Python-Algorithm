import heapq
import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = []
for i in range(n):
    m, v = map(int, sys.stdin.readline().split(" "))
    heapq.heappush(lst, (m, -v))
bags = deque(sorted([int(sys.stdin.readline()) for _ in range(k)]))
res = []
result = 0
print(lst)
for bag in bags:

    while lst and lst[0][0] <= bag:
        # 가방 무게로 넣을 수 있는 것들 다 res에 집어넣음
        heapq.heappush(res, heapq.heappop(lst)[1])
    # 해당 무게보다 적은 것들이 있음
    print(res)
    if res:
        result -= heapq.heappop(res)

