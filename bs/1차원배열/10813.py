import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N,M = map(int, input().split(" "))
lst = [i for i in range(N+1)]
for i in range(M):
    left, right = map(int,input().split(" "))
    tmp = lst[left]
    lst[left] = lst[right]
    lst[right] = tmp
for j in lst[1:]:
    print(j,end=" ")
