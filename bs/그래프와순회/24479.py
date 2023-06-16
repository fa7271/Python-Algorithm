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

res = [0] * (N+1)
cur = 1
def dfs(idx):
    global cur
    res[idx] = cur
    for i in sorted(graph[idx]):
        if res[i] == 0:
            cur += 1
            dfs(i)

dfs(R)
for i in res[1:]:
    print(i)
