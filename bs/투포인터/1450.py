import bisect
import sys
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, c = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
left = arr[:n // 2]
right = arr[n // 2:]

sumleft = []
sumlst2 = []

for i in range(len(left) + 1):
    sumleft += map(sum, combinations(left, i))
for i in range(len(right) + 1):
    sumlst2 += map(sum, combinations(right, i))
sumlst2.sort()
res = 0
for i in sumleft:
    if c - i < 0:
        continue
    res += bisect.bisect_right(sumlst2, c - i)
print(res)
