import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(sys.stdin.readline())
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(T):
    print(dp[int(sys.stdin.readline())])
# dp[4]  = dp[3] +dp[1] , dp[2] +

