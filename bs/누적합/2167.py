import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
dp = [[0] * (M + 1) for _ in range(N + 1)]

graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = graph[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
k = int(input())
for _ in range(k):
    x, y, nx, ny = map(int, sys.stdin.readline().split(" "))
    print(dp[nx][ny] - dp[x - 1][ny] - dp[nx][y - 1] + dp[x - 1][y - 1])
