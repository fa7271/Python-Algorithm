import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N =int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for i in range(N)]

dp = [0] * (N)
dp[0] = lst[0]
if N > 1:
    dp[1] = lst[0]+lst[1]
if N > 2:
    dp[2] = max(dp[1],lst[1]+lst[2],lst[0]+lst[2])

for i in range(3,N):
    dp[i] = max(lst[i]+lst[i-1]+dp[i-3], lst[i]+dp[i-2], dp[i-1])
print(dp[N-1])