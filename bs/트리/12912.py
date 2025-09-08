import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


# BFS 로 제일 먼거 찾아준다.
def BFS(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque([(start, 0)])  # 노드와 해당 노드까지의 가중치 값을 큐에 저장
    max_distance = (start, 0)  # 가장 먼 노드와 해당 노드까지의 가중치 값을 저장하는 변수

    while queue:
        node, distance = queue.popleft()
        visited[node] = distance

        for next_node, next_cost in graph[node]:
            if visited[next_node] == -1:
                new_distance = distance + next_cost
                queue.append((next_node, new_distance))

                if new_distance > max_distance[1]:  # 현재까지 가장 먼 노드보다 더 먼 노드를 발견하면 갱신
                    max_distance = (next_node, new_distance)

    return max_distance


def find_node(start):
    farthest_node, a = BFS(start)
    b, result = BFS(farthest_node)

    return result


n = int(input())
graph = [[] for _ in range(n)]
path = []
for _ in range(n - 1):
    u, v, e = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((v, e))
    graph[v].append((u, e))
    path.append((u, v, e))

rst = -1e9
for u, v, e in path:
    graph[u].remove((v, e))
    graph[v].remove((u, e))

    a = find_node(u)
    b = find_node(v)

    rst = max(rst, a + b + e)

    graph[u].append((v, e))
    graph[v].append((u, e))
print(rst)
