import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque

N = int(input())
dq = deque()

for i in range(N):
    x = sys.stdin.readline().rstrip().split()
    if x[0] == "1":
        dq.appendleft(x[1])
    elif x[0] == "2":
        dq.append(x[1])
    elif x[0] == "3":
        if dq:print(dq.popleft())
        else:print(-1)
    elif x[0] == "4":
        if dq:print(dq.pop())
        else: print(-1)
    elif x[0] == "5":
        print(len(dq))
    elif x[0] == "6":
        if dq: print(0)
        else: print(1)
    elif x[0] == "7":
        if dq:print(dq[0])
        else:print(-1)
    elif x[0] == "8":
        if dq : print(dq[-1])
        else: print(-1)
