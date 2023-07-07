import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# n, m = map(int, sys.stdin.readline().split())  # 건물 n, 도로 m
#
# graph = [[] * (n + 1) for _ in range(n + 1)]
# for i in range(m):
#     x,y = map(int,sys.stdin.readline().rstrip().split())
#     graph[x].append(y)
#     graph[y].append(x)
#
# def bfs(node1,node2):
#     Q = deque()
#     Q.append([node1,0])
#     Q.append([node2,0])
#     visited[node1] = True
#     visited[node2] = True
#     while Q:
#         node, depth= Q.popleft()
#         if scores[node] == 10000000:
#             scores[node] = min(scores[node],depth * 2)
#         for next_node in graph[node]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 Q.append([next_node, depth+1])
#         # 모든 노드를 방문하면서 깊이 * 2를 기록한다.
#     cases_score.append([node1,node2,scores[1::]])
#
# cases_score = []
# scores = [10000000 for _ in range(n+1)]
# chi = []
# for i in range(1, n):
#     for j in range(i+1, n+1):
#         visited = [False for _ in range(n+1)]
#         bfs(i,j)
# res = [[x,y,sum(z)] for x,y,z in cases_score]
# res.sort(key = lambda x:-x[2])
#
# print(res[0][0],res[0][1],res[0][2])

n, m = map(int, sys.stdin.readline().split())  # 건물 n, 도로 m
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신은 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
# 1. 모든 정점에서 모든 정점으로 가는  최소 거리 구하기
for k in range(1, n + 1):
    for a in range(1, n + 1):   # 출발 노드
        for b in range(1, n + 1):   # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


min_sum = INF
result = list()
for i in range(1, n):  # 건물 2개를 뽑는다.
    for j in range(2, n + 1):
        sum_ = 0
        for k in range(1, n + 1):  # 모든 집을 방문하면서 거리를 측정
            sum_ += min(graph[k][i], graph[k][j]) * 2  # k -> i, k -> j 중에 짧은 거리 합치기
        if sum_ < min_sum:
            min_sum = sum_
            result = [i, j, sum_]
print(result)