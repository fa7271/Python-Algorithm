import heapq
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
heap = []
heapq.heapify(heap)
length = 0
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    heapq.heappush(heap, (-b, a))
    length = max(length,a)

score = [False] * (length + 1)
res = 0
while heap:
    num, idx = heapq.heappop(heap)
    num = -num
    for idx in range(idx , 0, -1):
        if score[idx]:
            continue
        score[idx] = num
        res += num
        break
print(score)
print(res)
