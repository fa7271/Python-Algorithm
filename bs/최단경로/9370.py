import sys, heapq

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())


def dj(start):
    distance = [int(1e9)] * (n + 1)
    heap = []
    heapq.heappush(heap, (start, 0))
    distance[start] = 0
    while heap:
        cur_node, cur_w = heapq.heappop(heap)
        if distance[cur_node] < cur_w:
            continue
        for next_node, nex_w in graph[cur_node]:
            d = cur_w + nex_w
            if distance[next_node] > d:
                distance[next_node] = d
                heapq.heappush(heap, (next_node, d))
    return distance


for i in range(t):
    n, m, t = map(int, sys.stdin.readline().rstrip().split(" "))  # 각각 교차로, 도로, 목적지 후보
    s, g, h = map(int, sys.stdin.readline().rstrip().split(" "))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    destination = [int(input()) for _ in range(t)]

    S = dj(s)
    G = dj(g)
    H = dj(h)
    res = []
    for des in destination:
        if S[des] == S[g] + G[h] + H[des] or S[des] == S[h] + H[g] + G[des]:
            res.append(des)
    res.sort()
    for result in res:
        print(result, end=' ')
