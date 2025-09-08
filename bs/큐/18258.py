import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque
N = int(input())
lst = deque()
for _ in range(N):
    order = sys.stdin.readline().rstrip().split(" ")
    if order[0] == "push":
        lst.append(order[1])
    elif order[0] == "front":
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif order[0] == "pop":
        if len(lst)!=0:
            print(lst.popleft())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(lst))
    elif order[0] == "back":
        if lst:
            print(lst[-1])
        else:
            print(-1)
    elif order[0] == "empty":
        if len(lst) ==0:
            print(1)
        else:
            print(0)
