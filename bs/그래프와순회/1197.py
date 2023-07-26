import heapq
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N ,M = map(int,sys.stdin.readline().split(" "))
"""
크루스칼 알고리즘

graph = []
# 간선체크
for i in range(M):
    a, b, c = map(int,sys.stdin.readline().rstrip().split(" "))
    graph.append((a,b,c))
# 자기자신이 부모
parent = [i for i in range(N+1)]
graph.sort(key=lambda x:x[2])
def find(x):
    # 자기 자신이 부모가 아니면
    if x != parent[x] :
        parent[x] = find(parent[x])
    return parent[x]
res = 0
for x, y, c in graph:
    X = find(x)
    Y = find(y)
    # 사이클을 형성하지 않은경우
    if X != Y :
        # X 가 Y 보다 크면
        if X > Y :
            # 작은 수 가 부모임
            parent[X] = y
        else:
            parent[Y] = X
        res += c
print(res)
"""
# prim 알고리즘

visited = [False]*(N+1)
lst = [[] for _ in range(N+1)]
heap = [[0, 1]]

for _ in range(M):
    # 간선 , 가중치
    s, e, w = map(int, input().split())
    lst[s].append([w, e])
    lst[e].append([w, s])

count = 0
res = 0
while heap:
    if count == N:
        break
    a, b = heapq.heappop(heap)

    if not visited[b]:
        visited[b] = True
        res += a
        count += 1
        for i in lst[b]:
            heapq.heappush(heap,i)
print(res)