import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

import heapq
n, m = map(int, input().split())
array = [[] for i in range(n+1)]
indegree = [0] * (n+1)
heap = []
res = []
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    array[x].append(y)
    indegree[y] += 1
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)
while heap:
    num = heapq.heappop(heap)
    res.append(num)
    for i in array[num]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap,i)

for i in res:
    print(i, end=" ")


# heap=[]
# result=[]
#
# for _ in range(m):
#     x, y = map(int,  input().split())
#     array[x].append(y)
#     indegree[y] += 1 # 진입차수 진입차수가 0 이여야 큐에 삽입 가능
# print(array,indegree)
#
# for i in range(1, n+1):
#     if indegree[i] ==0:
#         heapq.heappush(heap, i)
# while heap: # heap 빌때까지 시행
#     data = heapq.heappop(heap)
#     result.append(data)
#     for y in array[data]:
#         indegree[y]-=1
#         if indegree[y]==0:
#             heapq.heappush(heap,y)
# for i in result:
#     print(i, end = ' ')


