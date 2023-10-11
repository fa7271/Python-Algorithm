import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n, m = map(int,input().split())
# m <= 100000 m <= 1000000 정점 < 간선 >> 크루스칼 알고리즘
graph = []
# 간선체크
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))
    graph.append((a, b, c))
graph.sort(key=lambda x:x[2]) # 간선기준 정렬
parents = [i for i in range(n+1)]

# 부모 찾기
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]
# 작은 부모로 합쳐주기
def union(x, y):
    X = find(x)
    Y = find(y)
    # 사이클을 형성하지 않은경우
    if X < Y :
        parents[Y] = X
    else:
        parents[X] = Y
result = 0
max_result = 0
for start, end ,cost in graph:
    # 부모가 다를경우 >> 싸이클 형성 안됨
    if find(start) != find(end):
        # 부모 합쳐줌
        union(start,end)
        result += cost
        max_result = max(cost,max_result)
print(result-max_result)
# 마을의 이장은 마을을 두 개의 분리된 마을로 분할할 계획을 가지고 있다.
# 1: 2개의 집합으로 나누어야함