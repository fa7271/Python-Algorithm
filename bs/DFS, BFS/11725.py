import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]

def dfs(x):
    for i in graph[x]:
        if visited[i] == 0: # 미방문
            visited[i] = x
            dfs(i)

q = deque()
q.append(1)
def bfs():
    while q:
        node = q.popleft()
        for n_node in graph[node]:
            if visited[n_node] == 0:
                visited[n_node] = node
                q.append(n_node)
for i in range(N-1):
    x, y = map(int,sys.stdin.readline().split(" "))
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (N+1)
print(graph)
# dfs(1)
bfs()

# for i in range(2,N+1):
#     print(visited[i])

# [[], [4, 6], [4], [6, 5], [1, 2, 7], [3], [3, 1], [4]]

