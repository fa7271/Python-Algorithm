import bisect
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().rstrip().split(" ")))

dp = [numbers[0]]
res = []
for i in numbers:
    if dp[-1] < i:
        dp.append(i)
        res.append((len(dp) - 1, i))
    else:
        temp = bisect.bisect_left(dp, i)
        dp[temp] = i
        res.append((temp, i))
result = []
index = len(dp) - 1
for i in range(len(res) - 1, -1, -1):
    if res[i][0] == index:
        result.append(res[i][1])
        index -= 1
print(len(dp))
print(*result[::-1])
