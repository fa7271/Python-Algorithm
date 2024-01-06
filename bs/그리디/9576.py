import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
for i in range(N):
    n, m = map(int, sys.stdin.readline().split(" "))

    visited = [False for i in range(n + 1)]
    lst = deque(sorted([list(map(int, sys.stdin.readline().split(" "))) for _ in range(m)], key=lambda x: x[0]))
    res = 0
    # 책이 있는 동안
    while lst:
        a, b = lst.popleft()
        for i in range(a, b + 1):
            if not visited[i]:
                res += 1
                visited[i] = True
                break
    print(res)
