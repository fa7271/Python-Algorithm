import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
graph = [[] * n for _ in range(n + 1)]
dist = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    Q = deque()
    Q.append(x)
    dist[x] = 1
    while Q:
        dx = Q.popleft()
        for next_node in graph[dx]:
            if dist[next_node] == 0:
                dist[next_node] = dist[dx] + 1
                Q.append(next_node)


bfs(1)

cnt = max(dist)
a = dist.index(cnt)
print(a, dist[a] - 1, dist.count(dist[a]))
