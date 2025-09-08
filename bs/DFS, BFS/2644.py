import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N =int(sys.stdin.readline())
x, y = map(int,sys.stdin.readline().split(" "))
m = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(m):
    a, b = map(int,sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N+1)
result = [0]*(N+1)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result[i] += result[v] + 1
            dfs(i)
dfs(x)

print(result[y]) if result[y] != 0 else print(-1)
