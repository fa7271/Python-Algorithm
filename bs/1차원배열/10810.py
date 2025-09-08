import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N,M = map(int, input().split(" "))

lst = [0]* N
for i in range(M):
    left, right, num = list(map(int,input().split(" ")))
    for j in range(left,right+1):
        lst[j-1] = num
for k in lst:
    print(k,end=" ")