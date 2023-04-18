import heapq
from collections import deque
def solution(n, edge):
    dist = [1] + [0] * (n - 1)
    graph = [[ ] for i in range(n)]
    q =deque([1])
    for x, y in edge:
        graph[x-1].append(y)
        graph[y-1].append(x)
    while q:
        l = len(q)
        for i in range(l):
            now = q.popleft()
            for e in graph[now-1]:
                if dist[e-1] == 0:
                    dist[e-1] = 1
                    q.append(e)
    return l





# print(solution(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

#  가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

