import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().split(" "))
INF = 1e9
dist = [INF] * (n + 1)
graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(m)]


def bfs(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            u, v, e = graph[j]
            if dist[u] != INF and dist[u] + e < dist[v]:
                dist[v] = dist[u] + e
                if i == n - 1:
                    return False
    return True


if bfs(1):
    for i in range(2, n+1):
        if dist[i]==INF:
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)
