import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

input = sys.stdin.readline
# input = int(sys.stdin.readline())

n, m = map(int, input().split())
s = []

def f():
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n + 1):
        if i in s:
            continue
        s.append(i)
        f()
        s.pop()
f()