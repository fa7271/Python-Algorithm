import heapq
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n, m, a, b, c = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
ls = []
INF = sys.maxsize
for _ in range(m):
    x, y, e = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append((y, e))
    graph[y].append((x, e))
    ls.append(e)
ls.sort()
ls = list(set(ls))
# 시작 가중치값, 시작 노드
def dijskra(limit):
    Q = []
    heapq.heappush(Q, [0, a])
    dist = [INF] * (n + 1)
    dist[a] = 0
    while Q:
        cur_w, cur_node = heapq.heappop(Q)
        if cur_w > dist[cur_node]:
            continue
        for next_node, next_w in graph[cur_node]:
            d = cur_w + next_w
            if dist[next_node] > d and next_w <= limit:
                dist[next_node] = d
                heapq.heappush(Q, (d, next_node))
    print(dist,dist[b])
    if dist[b] > c:
        return INF
    else:
        return dist[b]


left = 0;
right = len(ls) - 1
res = INF
while left <= right:
    mid = (left + right) // 2
    total = dijskra(ls[mid])
    if total == INF:
        left = mid + 1
    else:
        right = mid - 1
        res = min(ls[mid], res)
if res == INF:
    print(-1)
else:
    print(res)