import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
N = int(input())
dp = [0] * (N+1)
for i in range(1,N+1):
    if i == 1 :
        dp[1] = 1
    elif i == 2:
        dp[2] = 1
    else:
        dp[i] = dp[i-2] + dp[i-1]
print(dp[N])
