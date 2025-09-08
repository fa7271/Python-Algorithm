import sys
from collections import Counter, defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
graph = [[1e9] * (n+1) for _ in range(n+1)]
while True:
    x, y = map(int,sys.stdin.readline().split(" "))
    if x == -1 and y == -1:
        break
    graph[x][y] = graph[y][x] = 1
for i in range(1,n+1):
    graph[i][i] = 1
for k in range(1,n+1):
    for x in range(1,n+1):
        for y in range(1,n+1):
            if graph[x][y] > graph[x][k] + graph[k][y]:
                graph[x][y] = graph[x][k] + graph[k][y]
dic = defaultdict(list)
for idx,i in enumerate(graph[1::],start=1):
    dic[max(*i[1::])].append(idx)
dic1 = sorted(dic)
print(dic1[0], len(dic[dic1[0]]))
print(*dic[dic1[0]])