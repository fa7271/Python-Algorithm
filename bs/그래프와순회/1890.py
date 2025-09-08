import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for x in range(n):
    for y in range(n):
        if x == n - 1 and y == n - 1:
            break
        temp = graph[x][y]
        if x + temp < n:
            dp[x + temp][y] += dp[x][y]
        if y + temp < n:
            dp[x][y + temp] += dp[x][y]
print(dp[n-1][n-1])
