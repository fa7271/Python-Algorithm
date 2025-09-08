def solution(n, results):
    graph =[[0] * (n) for _ in range(n)]
    for i in results:
        graph[i[0]-1][i[1]-1] = 1 # 승리표시
        graph[i[1]-1][i[0]-1] = -1 # 패배표시
    # 승, 패 그래프 업데이트 플로이드
    for k in range(n): # via
        for i in range(n): # start
            for j in range(n): # end
                if graph[i][k] == graph[k][j] == 1: # start > via, via > end, start > end
                    graph[i][j] = 1
                    # 패배한 경로도 표시해줌.
                    graph[j][i] = graph[j][k] = graph[k][i] = -1

    res = 0
    for line in graph:
        if line.count(0) == 1:
            res += 1
    return res


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))