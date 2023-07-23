import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
graph = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for g in graph:
    print(*g)



