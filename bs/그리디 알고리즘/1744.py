import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

arr = deque(sorted([int(sys.stdin.readline()) for i in range(N)]))
new_lst = []
left, right = 0,N-1
res = 0
for i in range(0, len(arr)-1,2):
    if arr[i] < 1 and arr[i+1] < 1:
        res += arr[i] * arr[i+1]
        left += 2
for i in range(len(arr)-1,0,-2):
    if arr[i] > 1 and arr[i-1] > 1:
        res += arr[i] * arr[i-1]
        right -= 2
for i in range(left,right+1):
    res += arr[i]
print(res)