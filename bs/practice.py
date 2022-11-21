# import sys, heapq
# sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
#
# input = sys.stdin.readline
# V, E = map(int,input().split()) # 점 5개 간선 6개
# start = int(input()) # 시작점 1
# graph =[[] for _ in range(V+1)]
# dist = [float('inf')] * (V+1)
# dist[start] = 0
#
# for i in range(E):
#     u,v,w = map(int,input().split())
#     graph[u].append((v,w))
#
# heap = []
# heapq.heappush(heap,(0,start))
#
# while heap:
#     cur_w, cur_node = heapq.heappop(heap)
#
#     for to_node, to_w in graph[cur_node]:
#         dis = cur_w + to_w
#         if dis < dist[to_node]:
#             dist[to_node] = dis
#             heapq.heappush(heap,(dis, to_node))
#
# for i in dist[1:]:
#     print(i if i!=float('inf') else 'INF')

def get_divisor(n):
    data = []
    count =0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            data.append(i)
    data.append(n)
    return data

print(get_divisor(8))


