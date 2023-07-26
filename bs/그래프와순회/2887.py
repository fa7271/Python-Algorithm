import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

# 거리가 가까운 순서대로 행성을 이루어줌 .
X, Y, Z = [], [], []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().rstrip().split(" "))
    X.append((x, i))
    Y.append((y, i))
    Z.append((z, i))

# x, y, z 좌표를 기준으로 정렬
X.sort()
Y.sort()
Z.sort()

graph = []
for i in range(1, N):
    # x, y, z 좌표를 기준으로 정렬한 리스트에서 각 행성들 간의 간선 비용 계산
    x_cost = abs(X[i][0] - X[i-1][0])
    y_cost = abs(Y[i][0] - Y[i-1][0])
    z_cost = abs(Z[i][0] - Z[i-1][0])

    # (간선 비용, 행성 A 번호, 행성 B 번호) 형태의 튜플을 graph 리스트에 추가
    graph.append((x_cost, X[i][1], X[i-1][1]))
    graph.append((y_cost, Y[i][1], Y[i-1][1]))
    graph.append((z_cost, Z[i][1], Z[i-1][1]))

graph.sort()  # 간선 비용 기준으로 정렬 최솟값 기준으로 해야하므로 reverse 해줌
graph.sort(key =lambda x:-x[0])

parents = [i for i in range(N+1)]
def find(node):
    if node != parents[node]:
        parents[node] = find(parents[node])
    return parents[node]
def union(node1,node2):
    if node1 > node2:
        parents[node1] = node2
    else:
        parents[node2] = node1

res = 0
count = 0
while graph:
    s,e,w = graph.pop()
    if count == N:
        break
    node1 = find(e)
    node2 = find(w)
    if node1 != node2:
        union(node1,node2)
        count += 1
        res += s
print(res)







