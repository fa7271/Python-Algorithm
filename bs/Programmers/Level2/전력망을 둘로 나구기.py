기from collections import deque
def solution(n, wires):

    graph = [[] for _ in range(n+1)]
    res = n-1
    for u,v in wires:
        graph[u].append(v)
        graph[v].append(u)
    def bfs(start):
        visited = [0] * (n+1)
        q = deque([start])

        count , visited[start] = 1,1
        while q:
            node = q.popleft()
            for i in graph[node]:
                if not visited[i]:
                    visited[i] = 1
                    count +=1
                    q.append(i)
        return count
    for a, b in wires: # 한 곳 끊기
        graph[a].remove(b)
        graph[b].remove(a)
        res = min((bfs(a)-bfs(b)), res)
        # 복구
        graph[a].append(b)
        graph[b].append(a)

    return res

print(solution(	9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))





