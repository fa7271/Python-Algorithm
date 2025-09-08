import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
n = int(input())

graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        x = i + j
        dp[j][x] = 2 ** 32
        for k in range(j, x):
            print(k, graph[j][0],graph[k][1],graph[x][1])
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + graph[j][0] * graph[k][1] * graph[x][1])
print(dp[0][-1])
