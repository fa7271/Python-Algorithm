import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
# dp = [0, "SK", "CY", "SK"]
# for i in range(len(dp), n + 1):
#     if dp[i - 1] == "CY" or dp[i - 3] == "CY":
#         dp.append("SK")
#     else:
#         dp.append("CY")
print("CY" if n%2 == 0 else "SK")