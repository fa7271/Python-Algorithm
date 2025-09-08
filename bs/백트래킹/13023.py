import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, input().split(" "))
graph = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split(" "))
    graph[x].append(y)
    graph[y].append(x)


def bt(node, depth):
    visited[node] = True
    if depth == 4:
        print(1)
        exit()
    for next_node in graph[node]:
        if not visited[next_node]:
            bt(next_node, depth + 1)
    visited[node] = False


for i in range(n):
    visited = [False] * n
    bt(i, 0)

print(0)
