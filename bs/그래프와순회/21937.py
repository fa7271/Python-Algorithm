import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)
x = int(input())
visited = [False] * (n + 1)

count = 0


def dfs(node):
    global count
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            count += 1
            dfs(next_node)
dfs(x)
print(count)