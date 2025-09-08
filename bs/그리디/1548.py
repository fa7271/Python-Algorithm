import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n =int(input())
lst = sorted(list(map(int,sys.stdin.readline().split())))
res = 1
for i in range(n-1):
    for j in range(n-1,-1,-1):
        if j >= i+1 and lst[i] + lst[i+1] > lst[j]:
            res = max(res,j-i+1)
print(res)

