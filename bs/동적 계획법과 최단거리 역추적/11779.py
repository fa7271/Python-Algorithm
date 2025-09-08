import heapq
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
bus = int(input())
INF = 1e9
dist = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(bus):
    u, v, e = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((v, e))
start, end = map(int, sys.stdin.readline().rstrip().split())
dist[start] = 0

hq = []
heapq.heappush(hq, [start, 0])
path = [-1] * (n + 1)
while hq:
    cur_node, cur_w = heapq.heappop(hq)
    if dist[cur_node] < cur_w:
        continue
    for next_node, nex_w in graph[cur_node]:
        d = cur_w + nex_w
        if dist[next_node] > d:
            dist[next_node] = d
            heapq.heappush(hq, (next_node, d))
            path[next_node] = cur_node

print(dist[end])
res = []
while end != -1:
    res.append(end)
    end = path[end]

print(len(res))
print(*res[::-1])
