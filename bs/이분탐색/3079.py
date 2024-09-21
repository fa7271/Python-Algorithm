import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = [int(sys.stdin.readline()) for _ in range(n)]
left = min(lst)
right = max(lst) * m
res = 0

while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in lst:
        count += mid//i

    if count >= m:
        right -= 1
        res = mid
    else:
        left += 1
print(res)
