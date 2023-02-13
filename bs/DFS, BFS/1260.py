import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        q = queue.popleft()
        print(q, end=" ")
        for i in graph[q]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)


def dfs(v):
    visited[v] = True
    print(v,end=" ")
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    start, end = map(int,input().split(" "))
    graph[start].append(end)
    graph[end].append(start)

for i in graph:
    i.sort()


visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)





