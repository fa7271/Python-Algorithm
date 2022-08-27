import sys
sys.stdin = open('/Python/h.txt', 'r')


print(sum(list(map(int,input().split()))))