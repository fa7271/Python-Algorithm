import math
import sys
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# 크루스칼 알고리즘 노드가 작음
n = int(input())
parents = [i for i in range(n)]
lst = [list(map(float, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

# 모든 점 사이 간선 구해야함.
edges = []

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((math.sqrt((lst[i][0] - lst[j][0]) ** 2 + (lst[i][1] - lst[j][1]) ** 2), i, j))
edges.sort() # 간선 기준 오름차순
def find_parent(node):
    if parents[node] != node: # 자기자신이 부모가 아님, 부모가 있다.
        parents[node] = find_parent(parents[node]) # 부모의 부모 찾음
    return parents[node]
def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    # 작은 값이 부모
    if x < y :
        parents[y] = x
    else:
        parents[x] = y

result = 0
for edge in edges:
    e, x, y = edge
    if find_parent(x) != find_parent(y): # 부모가 다르면 사이클 형성 x
        union(x,y)
        result += e
print(round(result,2))
