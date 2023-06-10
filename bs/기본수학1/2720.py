import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')



N  = int(sys.stdin.readline())

lst = [25,10,5,1]
for i in range(N):
    money = int(sys.stdin.readline())
    res = [0] *4
    pay = 0
    while money != 0:
        res[pay] = money // lst[pay]
        money = money % lst[pay]
        pay += 1
    print(*res)



