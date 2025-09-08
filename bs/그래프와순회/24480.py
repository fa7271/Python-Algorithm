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

idx = 1
res = [0]* (N+1)
def dfs(n):

    global idx
    res[n] = idx
    for i in sorted(graph[n],reverse=True):
        if res[i] == 0: # 안 밟았으면
            idx += 1
            dfs(i)

dfs(1)
for i in res[1:]:
    print(i)


