import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')



N  = int(sys.stdin.readline())

dp = [0] * 17
dp[0] = 4
dp[1] = 9

for i in range(2, 17):
    dp[i] = (int((dp[i-1]** 0.5) + (2**(i-1))))**2
print(dp[N])


