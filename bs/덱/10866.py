import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque

N = int(input())
dq = deque()

for i in range(N):
    x = sys.stdin.readline().rstrip().split()

    if x[0] == "push_front":
        dq.appendleft(x[1])
    elif x[0] == "push_back":
        dq.append(x[1])
    elif x[0] == "pop_front":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq.popleft())
    elif x[0] == "pop_back":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq.pop())
    elif x[0] == "size":
        print(len(dq))
    elif x[0] == "empty":
        if len(dq) == 0:
            print("1")
        else:
            print("0")
    elif x[0] == "front":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq[0])
    elif x[0] == "back":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq[-1])