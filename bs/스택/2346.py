import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(input())
lst = deque(list(enumerate(map(int,sys.stdin.readline().rstrip().split(" ")),start= 1)))
res = []
while lst:
    idx, rotate = lst.popleft()
    res.append(idx)
    if rotate > 0 :
        lst.rotate(-(rotate - 1))
    else:
        lst.rotate(-rotate)
print(*res)
