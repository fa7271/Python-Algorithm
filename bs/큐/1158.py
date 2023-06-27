import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque

N, K = map(int,sys.stdin.readline().split(" "))

arr =deque([i for i in range(1,N+1)])
res = []
while arr:
    arr.rotate(-2)
    res.append(arr.popleft())
print("<", ', '.join(str(i) for i in res), ">", sep = '')