import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

a = int(input())
b = list(map(int,input().split()))
print(min(b),max(b))