import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque
sys.setrecursionlimit(10**6)
N,M,R = map(int,sys.stdin.readline().split())

graph = [[] * i for i in range(N+1)]

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

res = [0]*(N+1)
res[R] = 1
def bfs(x):
    idx = 1
    q = deque([x])
    while q:
        now = q.popleft()
        for i in sorted(graph[now]):
            if res[i] == 0:
                idx +=1
                res[i] = idx
                q.append(i)


bfs(R)
for i in res[1:]:
    print(i)


