import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N,K = map(int,sys.stdin.readline().split(" "))

lst = deque([i for i in range(1,N+1)])
result = []
while lst:
    for i in range(K-1):
        x = lst.popleft()
        lst.append(x)
    result.append(lst.popleft())

print("<",end='')
for i in range(len(result)-1):
    print("%d, "%result[i], end='')
print(result[-1], end='')
print(">")



