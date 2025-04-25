import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n + 1)]

# 양방향 간선 추가
for _ in range(n - 1):
    start, end, E = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[start].append((end, E))
    graph[end].append((start, E))


# 1. 제일 먼 노드 찾기
def DFS(node, cost, exclude=None):
    global temp
    for next_node, next_cost in graph[node]:
        if next_node == exclude:
            continue
        new_cost = cost + next_cost
        if new_cost > visited[next_node]:
            temp = new_cost
        if visited[next_node] == -1:
            visited[next_node] = new_cost
            DFS(next_node, new_cost, exclude)

# 아무 지점에서 가장 먼 노드
# 1번 노드를 일단 시작점으로 지정, 가장 먼 노드 찾아줄 예정
visited = [-1] * (n + 1)
visited[1] = 0
DFS(1, 0)
Node1 = visited.index(max(visited))

# 가장 먼 노드에서 제일 먼 노드
visited = [-1] * (n + 1)
visited[Node1] = 0
DFS(Node1, 0)
Node2 = visited.index(max(visited))

# 상대 노드를 제외하고 가장 먼 노드 찾기
temp = 0
visited = [-1] * (n + 1)
visited[Node1] = 0
DFS(Node1, 0, exclude=Node2)
res1 = max(visited)

temp = 0
visited = [-1] * (n + 1)
visited[Node2] = 0
DFS(Node2, 0, exclude=Node1)
res2 = max(visited)

print(max(res1, res2))

