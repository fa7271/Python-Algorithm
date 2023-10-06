import heapq
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

city = int(input())
bus = int(input())
graph = [[] for _ in range(city+1)]
dist = [float('inf')] * (city+1)
for _ in range(bus):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v, w))

start, end = map(int,sys.stdin.readline().split())
# 시작위치와 가중치
hq = [(start,0)]

while hq:
    # 현재위치와, 가중치
    w, n =  heapq.heappop(hq)

    # 기존 최단거리보다 멀면 걍 무시한다.
    if dist[w] < n:
        continue

    for to_n, to_w in graph[w]:
        # 다음 거리 체크
        di = n + to_w
        if di >= dist[to_n]:
            continue
        dist[to_n] = di
        # 최솟값이면 , 가중치와, 다음 노드 넘김
        heapq.heappush(hq,(to_n,di))
print(dist[end])
