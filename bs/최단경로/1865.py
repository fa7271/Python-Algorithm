import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

INF = 1e9
tc = int(input())


def solution(start, n):
    dist = [INF for _ in range(n + 1)]
    dist[start] = 0

    for i in range(n):
        for cur_node, next_node, e in graph:
            if dist[next_node] > e + dist[cur_node]:
                if i == n - 1:
                    print(dist)
                    return True
                dist[next_node] = e + dist[cur_node]
    return False


for i in range(tc):
    n, m, w = map(int, input().split(" "))
    graph = []

    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split(" "))
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split(" "))
        graph.append((s, e, -t))

    if solution(1, n):
        print("YES")
    else:
        print("NO")
