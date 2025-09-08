import heapq
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = sorted([list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)], key=lambda x: (x[0], x[1]))
heap = [lst[0][1]]

heapq.heapify(lst)

print(lst,heap)
for i in range(1, n):
    # 제일 빨리 끝나는 방 이후에 시작되면 방 한 개 더 필요 함.
    if heap[0] <= lst[i][0]:
        # 방 하나 추가 해준다.
        heapq.heappop(heap)
    # 그 사이에 시작되면 방이 필요함.
    heapq.heappush(heap, lst[i][1])
print(len(heap))