import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n,m = map(int,input().split())
x = sorted(list(map(int,input().split())))
result = []

def bt():
    if m == len(result):
        print(*result)
        return
    now = 0
    for i in range(n):
        if now != x[i]:
            result.append(x[i])
            now = x[i]
            bt()
            result.pop()
bt()