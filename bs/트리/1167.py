import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

V = int(sys.stdin.readline()) # 정점의 개수
graph = [[] for _ in range(V+1)]

for _ in range(V):
    c = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))
visited = [-1] * (V+1)
visited[1] = 0

def dfs(node,cost):

    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost
        if visited[next_node] == -1:
            visited[next_node] = new_cost
            dfs(next_node,new_cost)

dfs(1,0)
lst = sorted([(idx,i) for idx,i in enumerate(visited)], key = lambda x:-x[1])
idx = lst[0][0]

visited = [-1] * (V+1)
visited[idx] = 0
dfs(idx,0)
print(max(visited))
