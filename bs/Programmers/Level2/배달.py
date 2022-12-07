import heapq
def solution(N, road, K):

    graph = [[] for _ in range(N+1)]

    for i in range(len(road)):
        u, v, w = road[i]
        graph[u].append((v, w))
        graph[v].append((u,w)) # 양 방향 이기 때문

    dist = [float("inf") for _ in range(N+1)]
    dist[1] = 0
    hq = []
    heapq.heappush(hq,(0,1))
    while hq:
        cur_w,cur_node = heapq.heappop(hq)
        for to_node, to_w in graph[cur_node]:
            dis = cur_w + to_w
            if dis < dist[to_node] :
                dist[to_node]  = dis
                heapq.heappush(hq,(dis,to_node) )

    count = 0
    for i in dist[1:]:
        if i <= K:
            count += 1
    return count


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
