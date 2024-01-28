import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(input())
res = []
result = []

def check(node):
    if len(res) == 1:
        return True
    if res[-2] > node:
        return True
    else: return False

def bt(depth):
    global res
    for i in range(10):
        res.append(i)
        if check(i) == True:
            bt(depth+1)
            result.append(int(''.join(str(x) for x in res)))
        res.pop()
bt(0)
result.sort()
try:
    print(result[n])
except:
    print(-1)
