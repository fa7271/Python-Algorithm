import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
def d(n) :
    n = n + sum(map(int,str(n)))
    return n

notself = set()

for i in range(1,10001):
    notself.add(d(i))
for j in range(1,10001):
    if j not in notself:
        print(j)