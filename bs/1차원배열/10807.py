import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = input()
lust_N = list(map(int,input().split()))
print(lust_N.count(int(input())))
