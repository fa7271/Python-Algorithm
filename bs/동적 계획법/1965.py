import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
box = list(map(int, sys.stdin.readline().split(" ")))


dp = [1] * n

for i in range(n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[j] + 1,dp[i])
print(max(dp))