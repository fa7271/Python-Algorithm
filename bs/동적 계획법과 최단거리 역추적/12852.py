import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(sys.stdin.readline())
q = deque()
q.append([n])
ans = []
while q:
    lst = q.popleft()
    x = lst[0]
    if x == 1:
        ans = lst
        break

    if x % 3 == 0:
        q.append([x // 3] + lst)

    if x % 2 == 0:
        q.append([x // 2] + lst)

    q.append([x - 1] + lst)
print(len(ans) - 1)
print(*ans[::-1])