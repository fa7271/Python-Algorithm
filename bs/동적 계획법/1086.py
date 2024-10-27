import math
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
# 1. 시간 초과

# import math
# from itertools import permutations
# n = int(input())
# numbers = []
# for i in range(n):
#     numbers.append(str(input()))
# k = int(input())
# down = math.factorial(n)
# up = 0
# for i in permutations(numbers, n):
#     if int("".join(i)) % k == 0:
#         up += 1
# gcd_num = math.gcd(down, up)
#
# print(up // gcd_num, "/", down // gcd_num, sep='')


N = int(input())
arr = [int(input()) for _ in range(N)]
K = int(input())
# i번째 비트를 사용했을때 나머지가 j인 경우의 수
dp = [[0] * K for _ in range(1 << N)]
dp[0][0] = 1 # 아무숫자 사용하지 않았을경우 나머지가 0 인 경우
print(dp[0])
# 각 숫자 arr[l]에 대해, 현재 나머지 j를 사용할 때 나머지를 미리 계산.
# rest[l][j]는 l번째 숫자를 추가했을 때, 현재 나머지가 j일 경우의 새로운 나머지
# 모둘러의 연산 사용
rest = []
for l in range(N):
    temp = []
    for j in range(K):
        temp.append((j * (10 ** (len(str(arr[l]))) % K) + (arr[l] % K)) % K)
    rest.append(temp)
for i in range(1 << N):
    for l in range(N):
        # 이미 숫자가 사용됨
        if i & (1 << l):
            continue
        # 현재 나머지 기준 새로운 나머지 계산
        for j in range(K):
            # 추가 했을때 새로운 나머지
            next_val = rest[l][j]
            dp[i | (1 << l)][next_val] += dp[i][j]
p = dp[(1 << N) - 1][0]
q = sum(dp[(1 << N) - 1])
g = math.gcd(p, q)
print(p // g, "/", q // g, sep='')
