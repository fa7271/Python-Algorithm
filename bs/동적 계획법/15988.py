import sys, time

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())
dp = [0, 1, 2, 4]

for i in range(t):
    x = int(input())
    for j in range(len(dp), x+1):
        dp.append((
            dp[j-3] + dp[j-2] + dp[j-1]
        ) %1000000009 )
    print(dp[x])