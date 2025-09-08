import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')



n = int(input())
res = []
def bt(x):
    if n == len(res):
        print(*res)
        return
    for i in range(1,n+1):
        if i not in res:
            res.append(i)
            bt(x+1)
            res.pop()
bt(1)