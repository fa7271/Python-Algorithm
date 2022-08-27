import sys
from collections import Counter # 최빈값 구하는 클래스
sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


N = int(sys.stdin.readline())
array = []
for i in range(N):
    # x,y = map(int,input().split())
    # array.append((x,y))
    array.append(list(map(int,sys.stdin.readline().split())))
print(array)
array.sort(key = lambda x: (x[0],x[1]))

for i in array:
    print(i[0], i[1])


