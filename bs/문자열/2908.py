import sys
sys.stdin = open('/Python/h.txt', 'r')


a,b= input().split()
A = (a[::-1])
B = (b[::-1])

if A > B:
    print(A)
else:
    print(B)