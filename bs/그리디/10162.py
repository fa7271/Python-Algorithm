import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

lst = [300,60,10]
idx = 0
n = int(input())

if n%10 != 0:
    print(-1)
else:
    for i in [300,60,10]:
        print(n//i, end=' ')
        n %=  i