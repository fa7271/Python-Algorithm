import sys, heapq

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def dj(i):
    dist_[i][0] = 0
    hq = []
    heapq.heappush(hq, [0, i])
    while hq:
        cur_w, cur_node = heapq.heappop(hq)
        for to_node, to_w in graph[cur_node]:
            d = cur_w + to_w
            if d < dist_[to_node][k - 1]:
                dist_[to_node][k - 1] = d
                dist_[to_node].sort()
                heapq.heappush(hq, [d, to_node])


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, e = map(int, input().split())
    graph[u].append((v, e))

dist_ = [[sys.maxsize] * k for _ in range(n + 1)]
dj(1)
for i in dist_[1::]:
    print(i[k-1] if i[k-1] != sys.maxsize else -1)
