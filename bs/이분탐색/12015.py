import sys
from bisect import bisect_left

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
lst = [int(i) for i in sys.stdin.readline().split(" ")]

# 시간 초과 코드
# dp = [1] * N
# for i in range(N):
#     for j in range(i):
#         if lst[i] > lst[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

stack = []
for i in lst:
    if not stack or stack[-1] < i:
        stack.append(i)
    else:
        x = bisect_left(stack,i)
        stack[x] = i
    print(stack)
print(len(stack))
