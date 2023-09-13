import sys
from itertools import product

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
dp = [[0] * 10 for _ in range(N)] # dp[길이][시작수]
for i in range(10):
    dp[0][i] = 1
for i in range(1,N):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j::])
print(dp)
print(sum(dp[N-1])%10007)

#dp[2][1] 길이가 2이고 시작이 1인숫자, dp[1] 시작이 1,0 더해주면됨 dp[2][0] 이면 그대로
