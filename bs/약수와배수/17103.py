import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


import sys

t = int(input())

arr = [True for _ in range(1000001)]
for i in range(2,1001):
    if arr[i]:
        for j in range(i + i , 1000001, i):
            arr[j] = False

for i in range(t):
    res = 0
    n = int(sys.stdin.readline().rstrip())
    for j in range(2, n//2+1):
        if arr[j] and arr[n-j]:
            res += 1
    print(res)