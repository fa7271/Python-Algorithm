import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N,M = map(int,sys.stdin.readline().split(" "))
res = deque(list(map(int,sys.stdin.readline().split(" "))))
lst = deque([i for i in range(1,N+1)])

count = 0
while len(res) != 0:
    num = res.popleft()
    while True:
        if num == lst[0] :
            lst.popleft()
            break
        else:
            if lst.index(num) > len(lst)//2: # 절반보다 크면 오른쪽 아니면 왼쪽
                lst.rotate(1)
                count +=1
            else:
                lst.rotate(-1)
                count += 1
print(count)
# 2 9 5
# 1,2,3,4,5,6,7,8,9,10









