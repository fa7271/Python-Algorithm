import sys
sys.stdin = open('/Python/h.txt', 'r')

A,B,C = map(int,input().split())

if B>C:
    print(-1)
else:
    print(A//(C-B)+1)
