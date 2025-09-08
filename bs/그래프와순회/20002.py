import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
graph = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
for i in range(1, N+1):
    for j in range(1, N+1):
        graph[i][j] = graph[i][j-1] + graph[i-1][j] - graph[i-1][j-1] + graph[i][j]

result = graph[1][1]
for k in range(N):
    for i in range(1, N-k+1):
        for j in range(1, N-k+1):
            temp = graph[i+k][j+k] - graph[i-1][j+k] - graph[i+k][j-1] + graph[i-1][j-1]
            result = max(result, temp)

print(result)

