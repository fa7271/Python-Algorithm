import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')




N = int(sys.stdin.readline())

dic = dict()
for i in range(N):
    name, status = map(str,sys.stdin.readline().split(" "))

    if name not in dic:
        dic[name] = 1
    else:
        del dic[name]
sorted(dic,reverse=True)
for i in dic:
    print(i)

