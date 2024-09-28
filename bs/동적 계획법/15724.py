import sys, time

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().rstrip().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
li = [[0] * (m + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + li[i][j] - dp[i - 1][j - 1]
for _ in range(int(input().rstrip())):
    sx, sy, ex, ey = list(map(int, input().rstrip().split()))
    print(dp[ex][ey] - dp[sx - 1][ey] - dp[ex][sy - 1] + dp[sx - 1][sy - 1])
