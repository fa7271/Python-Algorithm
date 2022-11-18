import sys, heapq
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

input = sys.stdin.readline
V,E = map(int,input().split()) # vortex, edge
start = int(input())-1
dist = [float('inf')] * V # 양의 무한대
dist[start] = 0

graph = [[] for _ in range(V)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u-1].append((v-1, w))

hq = [(0, start)]
while hq:
    cur_w, cur_node = heapq.heappop(hq)
    for to_node, to_w in graph[cur_node]:
        d = cur_w + to_w
        if d < dist[to_node]:
            dist[to_node] = d
            heapq.heappush(hq, (d, to_node))

for i in dist:
    print(i if i!=float('inf') else 'INF')