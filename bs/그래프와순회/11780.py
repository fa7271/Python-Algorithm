import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

city = int(input())
bus = int(input())

graph = [[1e9]*(city+1) for _ in range(city+1)]
path = [[-1]*(city+1) for _ in range(city+1)]
for i in range(bus):
    a, b, e = map(int,sys.stdin.readline().rstrip().split(" "))
    graph[a][b] = min(graph[a][b],e)
    path[a][b] = a # 길 저장 a 에서 b 가는 길에 a

for i in range(1,city+1):
    for j in range(1,city+1):
        if i == j:
            graph[i][j] = 0
for k in range(1, city + 1): # 경유지
    for a in range(1, city + 1): # 출발지
        for b in range(1, city + 1): # 도착지
            # a > b 랑 a > k > b 중에 최솟값으로 바꿔줌
            d = graph[a][k] + graph[k][b]
            if graph[a][b] > d:
                graph[a][b] = d
                path[a][b] = path[k][b]
# 최소비용 출력
for i in range(1,city+1):
    for j in range(1,city+1):
        print(graph[i][j] if not graph[i][j] == 1e9 else 0, end=" ")
    print()
    
for i in range(1, city + 1):
    for j in range(1, city + 1):
        if graph[i][j] == 1e9 or graph[i][j] ==0:
            print(0)
        else:
            end = j
            lst = []
            while True:
                if end == i:
                    lst.append(i)
                    break
                lst.append(end)
                end = path[i][end]
            print(len(lst), end=" ")
