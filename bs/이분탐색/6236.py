import sys

sys.stdin = open('/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
arr = [int(input()) for _ in range(n)]

left = min(arr)
right = sum(arr)
result = 0
while left <= right:
    mid = (left + right) // 2
    temp_count = 1
    temp = mid
    for coin in arr:
        if temp < coin:
            temp = mid
            temp_count += 1
        temp -= coin
    if temp_count > m or mid < max(arr):
        left = mid + 1
    else:
        right = mid - 1
        result = mid
print(result)
