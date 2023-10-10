import heapq
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(N)]
# 최소거리
dist =[0] + [float('inf')] * (N-1)
A[-1] = 0
# 양방향 간선
for i in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append((b,t))
    graph[b].append((a,t))
hq = [(0,0)]
while hq:
    w, n = heapq.heappop(hq)
    if dist[w] < n:
        continue
    for to_node, to_w in graph[w]:
        di = n + to_w
        # 시야에 안 들어올때
        if A[to_node] == 0 and dist[to_node] > di:
            dist[to_node] = di
            heapq.heappush(hq, (to_node, di))
print(dist[N-1] if dist[N-1] != float('inf') else -1)
