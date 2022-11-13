import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())



def dp(n):
    dp = [0] * 101
    dp[1],dp[2] = 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-3] + dp[i-2]
    return dp[n]

for i in range(n):
    number = int(input())
    print(dp(number))

