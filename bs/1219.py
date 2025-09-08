import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, s, e, m = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(m)]

lst = list(map(int, sys.stdin.readline().rstrip().split()))
INF = -1e9
dist = [INF] * n

def Bellman_ford(s):
    dist[s] = lst[s]
    for i in range(n):
        for j in range(m):
            u, v, e = graph[j]
            if dist[u] != INF and dist[u] - e + lst[v] > dist[v]:
                dist[v] = dist[u] - e + lst[v]
    # 음의 사이클 찾기
    negative_cycle = [False] * n
    for u, v, e in graph:
        if dist[u] != INF and dist[u] - e + lst[v] > dist[v]:
            negative_cycle[v] = True
    # 음의 사이클과 연결된 것들 다 음의 사이클로 넣음
    for _ in range(n):
        for u, v, e in graph:
            if negative_cycle[u]:
                negative_cycle[v] = True

    return negative_cycle

res = Bellman_ford(s)
# 결과 출력
if dist[e] == INF:
    print("gg")
elif res[e]:
    print("Gee")
else:
    print(dist[e])