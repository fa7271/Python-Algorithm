import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())

lst = deque([i for i in range(1,N+1)])

while len(lst) > 1:
    lst.popleft()
    temp = lst.popleft()
    lst.append(temp)
print(lst[0])
