import sys,time

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
lst = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]
dp = [0] * (N+1)
for idx in range(1,N+1):
    t, p = lst[idx-1][0],lst[idx-1][1]
    dp[idx] = max(dp[idx], dp[idx - 1])
    # if idx + t -1 <= N:
    #     dp[idx + t -1] = max(dp[idx+t-1],dp[idx-1]+ p)
    # if dp[idx] < dp[idx-1] :
    #     dp[idx] = dp[idx-1]
    if idx + t > N:
        continue
    dp[idx+t-1] = max(dp[idx-1]+p, dp[idx+t-1])
print(dp)
print(max(dp))
