import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

A, B, C = map(int, sys.stdin.readline().rstrip().split())
total = A + B + C
# [A개수][B개수] C는 A-B
visited = [[False] * total for _ in range(total)]


def bfs():
    Q = deque([(A, B)])
    visited[A][B] = True
    while Q:
        na, nb = Q.popleft()
        nc = total - na - nb
        if na == nb == nc:
            print(1)
            exit()
        for a, b in (na, nb), (na, nc), (nb, nc):
            if a < b:
                b -= a
                a += a
            elif b < a:
                a -= b
                b += b
            else:
                continue
            c = total - a - b
            newX = min(a, b, c)
            newY = max(a, b, c)
            if not visited[newX][newY]:
                Q.append((newX, newY))
                visited[newX][newY] = True

    print(0)

if total % 3 != 0:
    print(0)
else:
    bfs()
