
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신은 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
# 최솟값 가는 간선이 1개가 아닐 수 도 있다
for _ in range(m):
    a, b, w  = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[a][b] = min(w, graph[a][b])
# 2. 플로이드 - 와샬 알고리즘
for k in range(1, n + 1): # 경유지
    for a in range(1, n + 1): # 출발지
        for b in range(1, n + 1): # 도착지
            # a > b 랑 a > k > b중에  최솟값으로 바꿔줌
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            1 > 4 a > 3 > 4
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("0",  end=" ")
        else:
            print(graph[a][b], end=" ")
    print()