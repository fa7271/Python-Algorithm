import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
import heapq


heap =[]
heapq.heapify(heap)

N = int(sys.stdin.readline())

for i in range(N):
    heapq.heappush(heap,int(sys.stdin.readline()))

if len(heap) == 1:
    print(0)
    exit()

sum = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum += a+b
    heapq.heappush(heap,a+b)

print(sum)

