import sys
from itertools import product
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))


count = 0
def bt(res):
    global count
    if len(res) == n:
        for i in lst:
            if i not in res:
                break
        else:
            count +=1
        return

    for i in range(10):
        res.append(i)
        bt(res)
        res.pop()

for i in range(10):
    res = []
    res.append(i)
    bt(res)
    res.pop()
print(count)