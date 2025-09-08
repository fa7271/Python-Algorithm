import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())

dp =[0,1,1,2,2,1,2,1]
dp.extend(0 for i in range(100001-8))
for i in range(8,N+1):
    dp[i] = min(dp[i-1], min(dp[i-2], min(dp[i-5], dp[i-7]))) +1
print(dp[N])
