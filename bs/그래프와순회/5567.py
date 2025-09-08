import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
import sys


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1) ]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [True] + [True] + [False] * (n)
count = 0
res = []
for i in graph[1]: # 1번이랑 연결된 노드
    count += 1
    visited[i] = True
    res.append(i)
for i in res:
    for x in graph[i]:
        if not visited[x]:
            count += 1
            visited[x] = True

print(count)