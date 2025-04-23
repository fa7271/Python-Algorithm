import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque

s, t = map(int, input().split())
if s == t:
    print(0)
    exit()

def calc(n, op):
    if op == '*':
        return n * n
    elif op == '+':
        return n + n
    elif op == '/':
        if n == 0:
            return -1
        return n // n

# BFS
q = deque()
q.append((s, ''))
visited = set()
visited.add(s)

while q:
    now, ops = q.popleft()

    for op in ['*', '+', '/']:
        nxt = calc(now, op)
        if nxt < 1 or nxt > 10**9 or nxt in visited:
            continue
        if nxt == t:
            print(ops + op)
            exit()
        visited.add(nxt)
        q.append((nxt, ops + op))

print(-1)
