from collections import deque

def solution(n, computers):

    graph = [[] for _ in range(n+1)]
    visited = [False] *(n+1)
    count = 0

    for idx, i in enumerate(computers):
        for j in range(len(i)):
            if computers[idx][j] == 1 and idx != j :
                graph[idx+1].append(j+1)



    for i in range(1,n+1):
        if visited[i] == False:
            dfs(i,graph,visited)
            count += 1
    return count

def dfs(start,graph,visited):
    visited[start] = True
    for e in graph[start]:
        if visited[e] == False:
            dfs(e,graph,visited)
    return visited

print(solution(	3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))