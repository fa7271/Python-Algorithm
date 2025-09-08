import sys
sys.stdin = open('/Python/h.txt', 'r')

a = int(input())
b = list(map(int,input().split()))
print(min(b),max(b))