import sys
from itertools import product

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n=int(input())



number_dic = {i:0 for i in range(1,6)}
lst = ['00','1']
for z in range(1,6):
    for i in product(lst, repeat=z):
        x = ''.join(i)
        if len(x) in number_dic:
            number_dic[len(x)] += 1
        else:
            pass
print(number_dic)

def dp(n):

    dp = [0] *1000001
    dp[1],dp[2] = 1, 2
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[n]

print(dp(n))



# 10000
# 00100
# 00001
# 10011
# 11100
# 11111
# 11001



# n = 짝수  00 뒤에 00 11/ 앞뒤사이로 00 /1 짝수갯수
# n = 홀수 1 앞뒤로 00 1 홀수개
#
# n = 1 >      1  >> 1
# n = 2 >  00, 11 >> 2
#
# n = 3 > 100,001, 111 >> 3
# n = 4 > 0011, 0000, 1001, 1100, 1111 >> 5
#
# n = 5 > 00100, 10000, 00001, 00100, 11111 >>
# n = 6 >