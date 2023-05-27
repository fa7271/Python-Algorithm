import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

import heapq

N = int(input())

heap =[]
heapq.heapify(heap)
for i in range(N):
    num = int(sys.stdin.readline())
    print(heap)
    if num == 0 :
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-num,num))




