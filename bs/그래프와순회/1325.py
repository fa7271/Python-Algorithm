import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    y, x = map(int, sys.stdin.readline().split())
    graph[x].append(y)

res = []

for i in range(1, n+1):
    visited = [False] * (n+1)
    q = deque([i])
    visited[i] = True

    count = 1

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
                count +=1
    res.append(count)

max_res = max(res)

for i in range(n):
    if res[i] == max_res:
        print(i+1, end=" ")