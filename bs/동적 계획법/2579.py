import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

dp = [0 for i in range(N)]
arr = [int(input()) for i in range(N)]

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0]+arr[1], arr[1]+arr[2])

for i in range(3,N):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
    print(arr[i-1])


