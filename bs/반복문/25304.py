import sys
sys.stdin = open('/Python/h.txt', 'r')

sum = int(input())
type = int(input())

res = 0
for i in range(type):
    a,b= map(int,input().split())
    res += a*b

if sum == res: print("Yes")
else:print("No")

