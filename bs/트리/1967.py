import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n + 1)]

# 양방향 간선 추가
for _ in range(n-1):
    start, end, E = map(int,sys.stdin.readline().rstrip().split(" "))
    graph[start].append((end,E))
    graph[end].append((start,E))

# 1번 노드를 일단 시작점으로 지정, 가장 먼 노드 찾아줄 예정
visited = [-1]*(n+1)
visited[1] = 0

# DFS 로 제일 먼거 찾아준다.
def DFS(node, cost):
    for next_node ,next_cost in graph[node]:
        new_cost = cost + next_cost
        if visited[next_node] == -1:
            visited[next_node] = new_cost
            DFS(next_node,new_cost)
DFS(1,0)
Node = (0,0)
for idx,value in enumerate(visited):
    if value > Node[1]:
        Node = (idx,value)

# 제일먼 노드와, 가중치 값
visited = [-1]*(n+1)
visited[Node[0]] = 0
DFS(Node[0], 0)
print(max(visited))

"""BFS
import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n + 1)]

# 양방향 간선 추가
for _ in range(n-1):
    start, end, E = map(int,sys.stdin.readline().rstrip().split(" "))
    graph[start].append((end,E))
    graph[end].append((start,E))

# 1번 노드를 일단 시작점으로 지정, 가장 먼 노드 찾아줄 예정
visited = [-1]*(n+1)
visited[1] = 0

# BFS 로 제일 먼거 찾아준다.
def BFS(start):
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

farthest_node, _ = BFS(1)  # 루트 노드인 1에서 시작하여 BFS 수행
visited = [-1] * (n + 1)  # 방문 배열 초기화
_, result = BFS(farthest_node)  # 두 번째 BFS를 수행하여 가장 먼 노드(farthest_node)로부터의 지름 구하기

print(result)  # 트리의 지름 출력

"""
