import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque
sys.setrecursionlimit(10**6)
N,M,R = map(int,sys.stdin.readline().split())

graph = [[] * i for i in range(N+1)]

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

res = [0]*(N+1)
q = deque([R])
res[R] = 1
count = 1
while q:
    now = q.popleft()
    for i in sorted(graph[now],reverse=True):
        if res[i] == 0:
            q.append(i)
            count += 1
            res[i] = count
for i in res[1:]:
    print(i)


