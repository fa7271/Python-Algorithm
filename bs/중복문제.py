import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

arr = [1, 2]
n = 2
res = []
for i in range(1 << n):
    temp = []
    for j in range(n):
        if i & (1 << j):
            continue
        temp.append(arr[j])
    res.append(temp)
print(res)