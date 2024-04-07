import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
dp = lst
min_dp = lst

for _ in range(n - 1):
    input_list = list(map(int, sys.stdin.readline().split(" ")))

    dp = [input_list[0] + max(dp[0], dp[1]), input_list[1] + max(dp), input_list[2] + max(dp[1], dp[2])]
    min_dp = [input_list[0] + min(min_dp[0], min_dp[1]), input_list[1] + min(min_dp), input_list[2] + min(min_dp[1], min_dp[2])]
print(max(dp),min(min_dp))