import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
M = int(input())

lst = [int(sys.stdin.readline()) for _ in range(M)]

dp = [0 for i in range(41)]
dp[0] = 1 ; dp[1] = 1; dp[2] = 2; dp[3] = 3
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
idx = 0

for i in lst:
    ans *= dp[i-idx-1] # 지금까지
    idx = i # 현재값 바꿔줌
print(N,idx)
print(ans * dp[N-idx])

