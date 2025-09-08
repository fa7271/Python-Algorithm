import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())
s, e = map(int, input().split())

graph = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))
graph.sort(key=lambda x: -x[0])
parent = [i for i in range(n + 1)]

res = 0


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[x] = y


for i in graph:
    c, x, y = i
    if find(s) != find(e):
        res = c
        union(x, y)

if find(s) == find(e):
    print(res)
else:
    print(0)
