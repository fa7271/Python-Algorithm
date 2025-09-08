import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, k = map(int, sys.stdin.readline().split(" "))
lst = sorted(list(map(int,sys.stdin.readline().split(" "))))
print(lst)
res = 0
while True:
    for i in range(k):
        if m == 0:
            break
        res += lst[-1]
        m -=1
    if m == 0:
        break
    res += lst[-2]
    m -= 1
print(res)