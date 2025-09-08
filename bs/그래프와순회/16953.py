import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

A, B = map(int,input().split())
count = 1
def bfs(A,cnt):
    if A <= B:
        if A == B:
            print(cnt)
            exit()
        bfs(A * 2,cnt+1)
        bfs(int(str(A)+"1"),cnt+1)
    return -1
print(bfs(A,count))
