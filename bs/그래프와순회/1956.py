import heapq,sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# v, e = map(int,input().split())
# graph =[[] for _ in range(v+1)]
#
# #거리저장 2차원 배열
# dist = [[1e9] * (v+1) for _ in range(v+1)]
# heap = []
# for _ in range(e):
#     a, b, c = map(int,input().split())
#     # 단방향
#     graph[a].append([b,c])
#     # a > b 가는 가중치 저장
#     dist[a][b] = c
#     heapq.heappush(heap,(c, a, b)) # 간선치 기준, 출발마을, 도착마을
#
# while heap:
#     d, a, b = heapq.heappop(heap)
#     # 싸이클 생성
#     if a == b:
#         print(d)
#         break
#
#     # 이미 저장된 비용보다 크면 필요 없음
#     if dist[a][b] < d:
#         continue
#     # a > b 는 이미 저장 되어있으므로
#     # b에서 다음 가는 경로를 검사해야함
#     # 도착지점, 가중치
#     for da, db in graph[b]:
#         # s > g > db
#         new_dist = d + db
#         # s > db
#         if new_dist < dist[a][da]:
#             dist[a][da] = new_dist
#             heapq.heappush(heap,(new_dist,a,da))
# else:
#     print(-1)

import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

v, e = map(int,input().split())
graph = [[1e9] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    a, b, w  = map(int, sys.stdin.readline().rstrip().split(" "))
    # 거리 저장
    graph[a][b] = w
# 2. 플로이드 - 와샬 알고리즘
for k in range(1, v + 1): # 경유지
    for a in range(1, v + 1): # 출발지
        for b in range(1, v + 1): # 도착지
            # a > b 랑 a > k > b중에  최솟값으로 바꿔줌
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 1e9
for i in range(1,v+1):
    result = min(result,graph[i][i])
print(result if result != 1e9 else -1)