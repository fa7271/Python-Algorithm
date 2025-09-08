import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, K = map(int,input().split(" "))
lst = list(map(int,(sys.stdin.readline().split(" "))))

dp = [0] * (N+1)

for i in range(N):
    dp[i+1] = dp[i] + lst[i]

for i in range(K):
    x, y = map(int,sys.stdin.readline().split(" "))
    print(dp[y] - dp[x-1])
