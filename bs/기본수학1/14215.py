import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

lst = sorted(list(map(int,sys.stdin.readline().split(" "))))
print(lst[0] + lst[1] + min(lst[2],lst[0]+lst[1] -1 ))


