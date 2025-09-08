import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

# dp= [i for i in range(50001)]
#
# for i in range(1,int(50001**0.5)+1):
#     dp[i*i] = 1
#
# for i in range(3,50001):
#     j = 1
#     while j*j <= i:
#         dp[i] = min(dp[i- j*j]+1, dp[i])
#         j += 1
# print(dp[n])
#


lst = sorted([ i*i for i in range(1,int(n**0.5)+1)], reverse=True)
count = 0
for i in lst:
    if n >= i:
        count += n // i
        n = n % i
print(count)
