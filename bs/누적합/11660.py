import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,sys.stdin.readline().split(" "))
dp = [[0] * (n+1) for i in range(n+1)]
maps =[list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(n)]

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + maps[i][j]
for i in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split(" "))
    print(dp[x2][y2], dp[x2][y1-1] , dp[x1-1][y2] , dp[x1-1][y1-1])
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])
