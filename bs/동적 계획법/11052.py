import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split(" ")))
dp = [0] *(N+1)

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j]+lst[j-1])
print(dp[N])