import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

A,B = map(int,input().split(" "))

lst = []
for i in range(1, B+1):
    for j in range(i):
        lst.append(i)

print(sum(lst[A-1:B]))