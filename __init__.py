import sys
from collections import deque
from itertools import product

import matplotlib.pyplot as plt

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
#
# n = int(input())
# x = deque(list(map(int, sys.stdin.readline().split(" "))))
# # 밑장 빼기는 한번.
#
# # 밑장 안뺌
# dp = 0
# for i in range(0, n, 2):
#     dp += x[i]
# result = dp
# dp1 = dp2 = dp
# for i in range(n - 1, 0, -1):
#     # 내가 밑장.
#     if i % 2:
#         dp1 += x[i]
#         dp1 -= x[i - 1]
#     # 니가 밑장
#     else:
#         dp2 -= x[i]
#         dp2 += x[i - 1]
#     result = max(dp1, dp2, result)
# print(result)
#

n, m = map(int, sys.stdin.readline().split(" "))
dp = [0] + list(map(int, sys.stdin.readline().split(" ")))
for i in range(1, n+1): #
    dp[i] += dp[i-1]
for _ in range(m):
    left, right = map(int, input().split(" "))
    result = (dp[right] - dp[left-1]) / (right - left + 1)
    print(f'{result:.2f}')
