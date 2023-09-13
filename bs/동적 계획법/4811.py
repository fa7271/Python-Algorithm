import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


dp = [[0] * 31 for _ in range(31)] # dp[w][h] 갯수
for i in range(1, 31):
    dp[0][i] = 1 # w, ww, www 이런 갯수를 말한다.
for i in range(1,31):
    for j in range(i,31):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
while True:
    N = int(input())
    if N == 0 :
        break
    print(dp[N][N])

