import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(input())
lst = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

dp = [0] * (n+1)
for i in range(1,n+1):
    t, p = lst[i-1][0], lst[i-1][1]
    if i+t-1 <= n:
        dp[i+t-1] = max(dp[i+t-1], dp[i-1] + p)
    if dp[i] < dp[i-1] :
        dp[i] = dp[i-1]
print(max(dp))