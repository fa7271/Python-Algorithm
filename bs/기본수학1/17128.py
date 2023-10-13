import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, q = map(int,input().split())
lst = deque(list(map(int, input().split())))
change_num = list(map(int,input().split()))
dp = [0] * n
# dp[0 -1 -2 -3]
for i in range(n):
    dp[i] = lst[i%n] * lst[(i+1)%n] * lst[(i+2)%n] * lst[(i+3)%n]
result = sum(dp)
for num in change_num:
    for j in range(num-3,num+1):
        dp[(j-1)%n] *= -1
        result += 2 * dp[(j-1)%n]
    print(result)
