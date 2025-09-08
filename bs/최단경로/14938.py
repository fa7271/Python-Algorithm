import sys, heapq

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, r = map(int, sys.stdin.readline().rstrip().split(" "))
t = list(map(int, sys.stdin.readline().rstrip().split(" ")))
dist = [[1e9] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split(" "))
    dist[a][b] = l
    dist[b][a] = l
for i in range(n):
    dist[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
res = 0

for i in dist[1:]:
    temp = 0
    for idx,j in enumerate(i):
        if j <=m:
            temp += t[idx-1]
    res = max(temp,res)
print(res)